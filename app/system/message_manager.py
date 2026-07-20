from app.ai.ai_engine import AIEngine


class MessageManager:

    def __init__(self, chat_area, main_window=None):
        self.chat_area = chat_area
        self.main_window = main_window
        self.ai_engine = AIEngine()

        # Welcome message
        self.send_ai_message("Hello! I am ready to help you.")

    def send_user_message(self, message):

        # 1. Show USER message
        self.chat_area.add_message("You", message)

        # 2. Get AI reply
        reply = self.ai_engine.generate_response(message)

        # 3. Show AI reply
        self.send_ai_message(reply)

        # 4. Update history sidebar
        if self.main_window:
            recent_commands = self.ai_engine.get_recent_commands()
            self.main_window.history_panel.update_history(recent_commands)

    def send_ai_message(self, message):
        self.chat_area.add_message("ai_Desk", message)

    def send_system_message(self, message):
        self.chat_area.add_message("System", message)