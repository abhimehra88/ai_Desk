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

        # Conversation memory
        self.conversation_history = []

        print("Gemini LLM Initialized")

    def generate(self, user_message):

        # Add current user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Keep only last 10 messages (5 user + 5 assistant approx)
        self.conversation_history = self.conversation_history[-10:]

        try:

            # Build conversation context
            context = self._build_context()

            # Send to Gemini
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=context
            )

            ai_text = response.text

            # Save AI reply in memory
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_text
            })

            return ai_text

        except Exception as error:

            error_text = str(error)

            # Rate limit handling
            if "429" in error_text:
                return (
                    "⚠️ AI requests are temporarily rate-limited. "
                    "Please try again in a few moments."
                )

            # Generic error
            return f"⚠️ AI service error: {error_text}"

    def _build_context(self):

        # System instruction
        context = (
            "You are ai_Desk, a desktop AI assistant with conversation memory. "
            "Use previous messages when answering follow-up questions. "
            "Be concise, practical, and context-aware.\n\n"
        )

        # Add conversation history
        for msg in self.conversation_history:

            role = "User" if msg["role"] == "user" else "Assistant"

            context += f"{role}: {msg['content']}\n"

        return context