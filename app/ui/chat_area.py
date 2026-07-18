import customtkinter as ctk


class ChatArea:

    def __init__(self, parent):
        self.parent = parent
        self.widget = self.create()

    def create(self):
        self.frame = ctk.CTkScrollableFrame(
            self.parent,
            corner_radius=12
        )
        self.frame.pack_propagate(True)

        self.add_message(
            "🤖 ai_Desk",
            "Hello! I am ready to help you."
        )

        return self.frame

    def add_message(self, sender, message):
        print(f">>> {sender}: {message}")

        container = ctk.CTkFrame(
            self.frame,
            fg_color="#2b2b2b",
            corner_radius=10
        )

        container.pack(
            fill="x",
            padx=10,
            pady=5
        )

        sender_label = ctk.CTkLabel(
            container,
            text=sender,
            font=("Segoe UI", 14, "bold")
        )

        sender_label.pack(
            anchor="w",
            padx=10,
            pady=(8,2)
        )

        message_label = ctk.CTkLabel(
            container,
            text=message,
            justify="left",
            wraplength=700
        )

        message_label.pack(
            anchor="w",
            padx=10,
            pady=(0,8)
        )

    def get_widget(self):
        return self.widget