import customtkinter as ctk


class ChatArea:
    def __init__ (self,parent):
        self.frame = ctk.CTkFrame(parent)

        self.textbox = ctk.CTkTextbox(
            self.frame,
            font=("Segoe UI",15)
        )

        self.textbox.pack(fill="both",expand=True,padx=15,pady=15)

        self.textbox.insert(
            "end",
            "🤖 Welcome to ai_Desk!\n\nHow can I help you today?\n"
        )

        self.textbox.configure(state="disabled")

    def get_widget(self):
        return self.frame