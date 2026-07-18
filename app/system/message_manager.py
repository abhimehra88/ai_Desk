from app.ai.ai_engine import AIEngine


class MessageManager:

    def __init__(self, chat_area):
        self.chat_area = chat_area
        self.ai_engine = AIEngine()

    def send_user_message(self, message):
        self.chat_area.add_message(
            "👤 You",
            message
        )

        reply = self.ai_engine.generate_response(message)

        self.chat_area.add_message(
            "🤖 ai_Desk",
            reply
        )