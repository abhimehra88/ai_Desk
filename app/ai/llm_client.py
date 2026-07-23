import os
from dotenv import load_dotenv
from google import genai

from app.ai.ollama_provider import OllamaProvider
from app.ai.response_formatter import ResponseFormatter


class LLMClient:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        # Cloud AI
        self.client = genai.Client(api_key=api_key)

        # Local AI
        self.local_ai = OllamaProvider()

        # Conversation memory
        self.conversation_history = []

        # =========================
        # Gemini system prompt
        # =========================
        self.system_prompt = """
You are ai_Desk, a general AI desktop assistant with strong expertise in programming, DSA, Java, Python, software engineering, and B.Tech subjects.

Your goal is to be USEFUL, CLEAR, PRACTICAL, and HUMAN-FRIENDLY.

RESPONSE RULES:

- Answer the question directly in the first sentence.
- Keep most answers between 4-8 lines.
- Use simple Hindi-English mix when it improves understanding.
- For programming questions:
  1. Give a short definition.
  2. Give one tiny Java example.
  3. Give one key interview/exam point.
- Avoid long textbook explanations.
- Avoid unnecessary analogies.
- Avoid robotic phrases like "As an AI language model".
- For current news, sports, prices, or live information, rely on web-search evidence when provided.
- If information is uncertain, clearly say what is confirmed and what is unverified.
- For comparisons, use a table.
- You have broad general knowledge beyond B.Tech subjects.

Example style:

Question: What is recursion?

Answer:
Recursion means a function calls itself.

Java example:

int fact(int n){
    if(n == 1) return 1;
    return n * fact(n - 1);
}

Key point: Every recursive function must have a base case to stop infinite calls.
"""

        # =========================
        # Lightweight local prompt
        # =========================
        self.local_prompt = """
You are ai_Desk.

Answer briefly and clearly.

Rules:
- Use simple Hindi-English mix.
- For short questions: 3-6 lines.
- For programming questions:
  - Definition
  - Tiny Java example
  - One key point
- Avoid long analogies.
- Avoid filler like "Let's dive into".
- Avoid incomplete code.
- Keep answers practical and easy to understand.
"""

        print("LLM Stack Initialized (Gemini + Ollama)")

    # =====================================================
    # MAIN GENERATE METHOD
    # =====================================================

    def generate(self, user_message: str) -> str:

        # Save current user message
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Keep last 10 messages
        self.conversation_history = self.conversation_history[-10:]

        try:

            # Build Gemini context
            instruction = ResponseFormatter.build_instruction(user_message)

            context = (
                self._build_context()
                +"\n\nFormatting instruction:\n"
                + instruction
            )

            # Gemini request
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=context
            )

            ai_text = response.text.strip()
            ai_text = ResponseFormatter.clean(ai_text)
            ai_text = ResponseFormatter.make_human(user_message, ai_text)

            # Save AI reply
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_text
            })

            return ai_text

        except Exception as error:

            error_text = str(error)

            print(f"[GEMINI ERROR] {error_text}")
            print("[FALLBACK] Switching to local Gemma...")

            # Use ONLY current message for local model
            instruction = ResponseFormatter.build_instruction(user_message)

            local_input = (
                f"{self.local_prompt}\n\n"
                f"{instruction}\n\n"
                f"User: {user_message}"
            )

            local_reply = self.local_ai.generate(local_input)
            local_reply = ResponseFormatter.clean(local_reply)
            local_reply = ResponseFormatter.make_human(user_message, local_reply)
            
            # Clean local response
            local_reply = self._clean_local_response(local_reply)

            # Save local reply
            self.conversation_history.append({
                "role": "assistant",
                "content": local_reply
            })

            return local_reply

    # =====================================================
    # CONTEXT BUILDER
    # =====================================================

    def _build_context(self) -> str:

        context = self.system_prompt.strip() + "\n\n"

        for msg in self.conversation_history:

            role = "User" if msg["role"] == "user" else "Assistant"

            context += f"{role}: {msg['content']}\n"

        return context

    # =====================================================
    # LOCAL RESPONSE CLEANER
    # =====================================================

    def _clean_local_response(self, text: str) -> str:

        if not text:
            return "I couldn't generate a local response right now."

        # Remove common filler
        fillers = [
            "Alright then",
            "Let's dive into",
            "Think of it like",
            "Pocket Guide",
            "😊",
            "😄",
            "😁",
            "🚀"
        ]

        for filler in fillers:
            text = text.replace(filler, "")

        # Remove excessive blank lines
        lines = [line.rstrip() for line in text.splitlines()]

        cleaned_lines = []
        previous_empty = False

        for line in lines:

            is_empty = line.strip() == ""

            if is_empty and previous_empty:
                continue

            cleaned_lines.append(line)
            previous_empty = is_empty

        text = "\n".join(cleaned_lines).strip()

        # Limit extreme verbosity
        if len(text) > 1800:
            text = text[:1800] + "\n\n[Answer shortened]"

        return text