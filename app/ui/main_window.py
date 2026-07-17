from app.ui.input_bar import InputBar
from app.ui.chat_area import ChatArea
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
        title.pack(pady=(30,10))

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

        # Chat Area
        chat_area = ChatArea(self.root)
        chat_area.get_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Input Bar
        self.input_bar = InputBar(self.root)
        self.input_bar.get_widget().pack(
            fill="x",
            padx=20,
            pady=(0,20)
        )