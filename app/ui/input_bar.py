import customtkinter as ctk


class InputBar:
    def __init__ (self,parent):
        self.frame = ctk.CTkFrame(parent)

        self.entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Type your message.."
        )
        
        self.send_button = ctk.CTkButton(
            self.frame,
            text="Send"
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10,5),
            pady=10
        )

        self.send_button.pack(
            side="right",
            padx=(5,10),
            pady=10
        )

    def get_widget(self):
        return self.frame