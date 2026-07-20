import os
from dotenv import load_dotenv
from google import genai


class LLMClient:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        self.client = genai.Client(api_key=api_key)

        print("Gemini LLM Initialized")

    def generate(self, user_message):

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message
            )

            return response.text

        except Exception as error:

            error_text = str(error)

            if "429" in error_text:
                return (
                    "⚠️ AI requests are temporarily rate-limited. "
                    "Please try again in a few moments."
                )

            return f"⚠️ AI service error: {error_text}"