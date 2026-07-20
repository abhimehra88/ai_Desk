from app.ai.ai_engine import AIEngine


class MessageManager:

    def __init__(self, chat_area, main_window):
        self.chat_area = chat_area
        self.main_window = main_window
        self.ai_engine = AIEngine()

    def send_user_message(self, message):

        #Show user message
        self.chat_area.add_message(
            "👤 You",
            message
        )

        # Generate AI response
        reply = self.ai_engine.generate_response(message)

        # ShowAI response
        self.chat_area.add_message(
            "🤖 ai_Desk",
            reply
        )

        # Update history panel
        recent_commands = self.ai_engine.memory.get_recent_commands()
        self.main_window.update_history(recent_commands)

    def send_system_message(self, message):
        self.chat_area.add_message(
            "⚙️ System",
            message
    )