import customtkinter as ctk


class MainWindow:
    def __init__(self,root):
        self.root = root
        self.build_ui()
        
    def build_ui(self):
        # Title
        title = ctk.CTkLabel(
            self.root,
            text="ai_Desk",
            font=("Swegoe UI",32,"bold")
        )

        # Subtitle
        subtitle = ctk.CTkLabel(
            self.root,
            text="Your Intelligent Desktop",
            font=("Segoe UI",16)
        )
        subtitle.pack()
    
        # Welcome Message
        welcome = ctk.CTkLabel(
            self.root,
            text="What can I do for you today?",
            font=("Segoe UI",16)
        )
        welcome.pack(pady=(20,30))