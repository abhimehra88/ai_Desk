from app.system.system_commands import SystemCommands
from datetime import datetime


class AIEngine:

    def __init__(self):
        print("AI Engine Initialized")

        self.system = SystemCommands()

    def generate_response(self, message):

        message = message.lower().strip()

        intent = self.detect_intent(message)

        return self.handle_intent(intent, message)

    def detect_intent(self, message):

        if message in ["hi", "hello", "hey"]:
            return "greeting"

        if "time" in message:
            return "time"

        if "date" in message:
            return "date"

        if message in ["who are you", "about yourself"]:
            return "identity"
        
        if message.startswith("open"):
            return "system"

        return "unknown"

    def handle_intent(self, intent, message):

        if intent == "greeting":
            return self.handle_greetings(message)

        if intent == "time":
            return self.handle_time(message)

        if intent == "date":
            return self.handle_date(message)

        if intent == "identity":
            return self.handle_identity(message)
        
        if intent == "system":
            return self.system.execute(message)

        return self.handle_fallback(message)

    def handle_greetings(self, message):
        return "Hello! How can I help you today?"

    def handle_time(self, message):
        return datetime.now().strftime("%I:%M %p")

    def handle_date(self, message):
        return datetime.now().strftime("%d %B %Y")

    def handle_identity(self, message):
        return "I am ai_Desk, your intelligent desktop assistant."

    def handle_fallback(self, message):
        return f"You said: {message}"