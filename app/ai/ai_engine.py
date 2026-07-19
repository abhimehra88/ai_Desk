from datetime import datetime
from app.system.system_commands import SystemCommands


class AIEngine:

    def __init__(self):
        print("AI Engine Initialized")
        self.system = SystemCommands()

        self.last_action = None

    def generate_response(self, message):

        message = message.lower().strip()

        # =========================
        # CONTEXT MEMORY
        # =========================
        repeat_command = [
            "open it again",
            "repeat last action",
            "open previous app",
            "launch previous app",
            "do it again"
        ]

        if message in repeat_command:
            if not self.last_action:
                return "No previous action found."
            
            if self.last_action["type"] == "app":
                app = self.last_action["value"]
                success, response = self.system.open_app(app)
                return f"Repeating previous action: {response}"
            
            if self.last_action["type"] == "website":
                success, response = self.system.open_website(self.last_action["value"])
                return f"Repeating previous action: {response}"

        # =========================
        # APP LAUNCH HANDLER
        # =========================
        app_name = SystemCommands.extract_app_name(message)

        if app_name:
            success, response = self.system.open_app(app_name)

            if success:
                self.last_action = {
                    "type": "app",
                    "value": app_name
                }
            return response
        
        # =========================
        # WEBSITE HANDLER
        # =========================
        success, response = self.system.open_website(message)

        if success:
            self.last_action = {
                "type": "website",
                "value": message
            }
            return response
        
        # =========================
        # FOLDER HANDLER
        # =========================
        success, response = self.system.open_folder(message)

        if success:
            return response

        # =========================
        # EXISTING INTENT SYSTEM
        # =========================
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

        if message.startswith("open "):
            return "system"

        return "unknown"

    def handle_intent(self, intent, message):

        if intent == "greeting":
            return self.handle_greetings()

        if intent == "time":
            return self.handle_time()

        if intent == "date":
            return self.handle_date()

        if intent == "identity":
            return self.handle_identity()

        if intent == "system":
            return self.system.execute(message)

        return self.handle_fallback(message)

    def handle_greetings(self):
        return "Hello! How can I help you today?"

    def handle_time(self):
        return datetime.now().strftime("%I:%M %p")

    def handle_date(self):
        return datetime.now().strftime("%d %B %Y")

    def handle_identity(self):
        return "I am ai_Desk, your intelligent desktop assistant."

    def handle_fallback(self, message):
        return f"You said: {message}"