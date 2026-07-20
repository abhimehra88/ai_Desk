import customtkinter as ctk
from app.voice.voice_input import VoiceInput


class InputBar:

    def __init__(self, parent):
        self.parent = parent
        self.voice_input = VoiceInput()
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
            command=self.start_voice_input
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


    def start_voice_input(self):

        print("🎤 Voice button clicked")

        if not hasattr(self, "message_manager"):
            return
        
        try:
            
            # Show listening status
            self.message_manager.send_system_message(
                "🎤 Listening... Speak now."
            )

            # Covert speech to text
            text = self.voice_input.listen()

            # Normalize text
            text = text.lower().strip()

            print(f"VOICE DETECTED: {text}")

            if not text:
                self.message_manager.send_system_message(
                    "⚠️ No speech detected."
                )
                return 
            
            # Put text into input box
            self.entry.delete(0, "end")
            self.entry.insert(0, text)

            # Auto send
            self.send_message()

        except Exception as error:
            print(f"VOICE ERROR: {error}")

            self.message_manager.send_system_message(
                f"❌ Voice error: {str(error)}"
            )


        
            