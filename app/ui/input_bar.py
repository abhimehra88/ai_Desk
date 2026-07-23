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
            height=78,
            corner_radius=28,
            fg_color="#111827",
            border_width=1,
            border_color="#334155"
        )

        frame.pack_propagate(False)

        # =========================
        # TEXT INPUT
        # =========================
        self.entry = ctk.CTkTextbox(
            frame,
            height=52,
            corner_radius=12,
            wrap="word",
            fg_color="#0B1220",
            border_width=1,
            border_color="#334155",
            text_color="#F8FAFC",
            font=ctk.CTkFont(size=15)
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 10),
            pady=15
        )

        # Placeholder
        self.placeholder = "Ask anything, control your PC, or use voice…"

        self.entry.insert("1.0", self.placeholder)
        self.entry.configure(text_color="#64748B")

        # Keyboard bindings
        self.entry.bind("<Return>", self.on_enter_pressed)
        self.entry.bind("<Shift-Return>", self.allow_newline)

        # Focus bindings
        self.entry.bind("<FocusIn>", self.on_entry_focus)
        self.entry.bind("<FocusOut>", self.on_entry_unfocus)

        # =========================
        # VOICE BUTTON
        # =========================
        self.voice_button = ctk.CTkButton(
            frame,
            text="🎤",
            width=54,
            height=50,
            corner_radius=18,
            fg_color="#1D4ED8",
            hover_color="#2563EB",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.start_voice_input
        )

        self.voice_button.pack(
            side="left",
            padx=(0, 10)
        )

        # =========================
        # SEND BUTTON
        # =========================
        self.send_button = ctk.CTkButton(
            frame,
            text="➤",
            width=54,
            height=50,
            corner_radius=18,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=ctk.CTkFont(size=20, weight="bold"),
            command=self.send_message
        )

        self.send_button.pack(
            side="right",
            padx=(0, 15)
        )

        return frame

    # =====================================
    # BASIC
    # =====================================

    def get_widget(self):
        return self.widget

    def set_chat_area(self, chat_area):
        self.chat_area = chat_area
        print("ChatArea connected")

    def set_message_manager(self, message_manager):
        self.message_manager = message_manager

    # =====================================
    # PLACEHOLDER HANDLING
    # =====================================

    def on_entry_focus(self, event):

        current = self.entry.get("1.0", "end-1c").strip()

        if current == self.placeholder:
            self.entry.delete("1.0", "end")
            self.entry.configure(text_color="#F8FAFC")

    def on_entry_unfocus(self, event):

        current = self.entry.get("1.0", "end-1c").strip()

        if not current:
            self.entry.insert("1.0", self.placeholder)
            self.entry.configure(text_color="#64748B")

    # =====================================
    # KEYBOARD
    # =====================================

    def on_enter_pressed(self, event):

        # Enter = Send
        self.send_message()

        # Prevent newline insertion
        return "break"

    def allow_newline(self, event):

        # Shift+Enter = New line
        return None

    # =====================================
    # SEND MESSAGE
    # =====================================

    def send_message(self):

        print("Send button clicked")

        # Get textbox content
        message = self.entry.get("1.0", "end-1c").strip()

        print(message)

        # Ignore placeholder
        if message == self.placeholder:
            return

        # Ignore empty message
        if not message:
            return

        # Send to AI
        self.message_manager.send_user_message(message)

        # Clear textbox
        self.entry.delete("1.0", "end")

        # Keep focus
        self.entry.focus()

    # =====================================
    # VOICE INPUT
    # =====================================

    def start_voice_input(self):

        print("🎤 Voice button clicked")

        if not hasattr(self, "message_manager"):
            return

        try:

            # Show listening status
            self.message_manager.send_system_message(
                "🎤 Listening... Speak now."
            )

            # Speech → text
            text = self.voice_input.listen()

            if not text:
                self.message_manager.send_system_message(
                    "⚠️ No speech detected."
                )
                return

            # Normalize
            text = text.lower().strip()

            print(f"VOICE DETECTED: {text}")

            # Put text into textbox
            self.entry.delete("1.0", "end")
            self.entry.insert("1.0", text)
            self.entry.configure(text_color="#F8FAFC")

            # Auto send
            self.send_message()

        except Exception as error:

            print(f"VOICE ERROR: {error}")

            self.message_manager.send_system_message(
                f"❌ Voice error: {str(error)}"
            )