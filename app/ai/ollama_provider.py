import requests


class OllamaProvider:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "gemma3:1b"

    def generate(self, user_prompt: str) -> str:

        system_prompt = f"""
You are ai_Desk, a concise desktop AI assistant.

Rules:
- Answer in simple Hindi-English mix.
- For short questions, keep answers under 6 lines.
- For teaching requests, use:
  1. Short definition
  2. Small Java example
  3. One key interview/exam point
- Do NOT use unnecessary analogies.
- Do NOT repeat the same idea.
- Do NOT write incomplete code.
- Use clean formatting with headings and bullets.

User request:
{user_prompt}
"""

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": system_prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.2,
                        "num_predict": 220,
                        "top_p": 0.9
                    }
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "No response from local AI").strip()

        except Exception as error:
            return f"Local AI error: {str(error)}"