class MessageManager:


    def __init__ (self, chat_area):
        self.chat_area = chat_area

    def send_user_message(self, message):
        self.chat_area.add_message(
            "👤 You",
            message
        )

        reply = self.generate_reply(message)

        self.chat_area.add_message(
            "🤖 ai_Desk",
            reply
        )

    
    def generate_reply(self, message):
        return f"You said: {message}"