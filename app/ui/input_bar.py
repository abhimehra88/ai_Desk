import customtkinter as ctk


class InputBar:

    def __init__(self, parent):
        self.parent = parent
        self.widget = self.create()

    def create(self):
        frame = ctk.CTkFrame(
            self.parent,
            height=70,
            corner_radius=12
        )

        frame.pack_propagate(False)

        self.entry = ctk.CTkEntry(
            frame,
            placeholder_text="Type your message...",
            height=40
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 10),
            pady=15
        )

        self.entry.bind("<Return>", self.on_enter_pressed)

        self.voice_button = ctk.CTkButton(
            frame,
            text="🎤",
            width=50,
            height=40,
            command=self.voice_input_placeholder
        )

        self.voice_button.pack(
            side="left",
            padx=(0, 10)
        )

        self.send_button = ctk.CTkButton(
            frame,
            text="Send",
            command=self.send_message,
            width=80,
            height=40
        )

        self.send_button.pack(
            side="right",
            padx=(0, 15)
        )

        return frame

    def get_widget(self):
        return self.widget
    

    def set_chat_area(self, chat_area):
        print("ChatArea connected")
        self.chat_area = chat_area

    def on_enter_pressed(self, event):
        self.send_message()

    def send_message(self):
        print("Send button clicked")
        
        message = self.entry.get().strip()
        print(message)

        if not message:
            return
        
        self.message_manager.send_user_message(message)

        self.entry.delete(0,"end")
        self.entry.focus()

    
    def set_message_manager(self, message_manager):
        self.message_manager = message_manager


    def voice_input_placeholder(self):
        print("Voice input button clicked")

        if hasattr(self, "message_manager"):
            self.message_manager.send_system_message(
                "🎤 Voice input feature will be added in the next version."
            )
        
            