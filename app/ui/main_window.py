import customtkinter as ctk

from app.ui.chat_area import ChatArea
from app.ui.input_bar import InputBar


class MainWindow:
    def __init__(self, root):
        self.root = root

        self.build_ui()

    def build_ui(self):
        self.create_main_container()
        self.create_header()
        self.create_chat_area()
        self.create_input_bar()

    def create_main_container(self):
        self.main_container = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        self.main_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def create_header(self):
        self.title_label = ctk.CTkLabel(
            self.main_container,
            text="ai_Desk",
            font=("Segoe UI", 32, "bold")
        )
        self.title_label.pack(pady=(30, 10))

        self.subtitle_label = ctk.CTkLabel(
            self.main_container,
            text="Your Intelligent Desktop",
            font=("Segoe UI", 16)
        )
        self.subtitle_label.pack()

        self.welcome_label = ctk.CTkLabel(
            self.main_container,
            text="What can I do for you today?",
            font=("Segoe UI", 16)
        )
        self.welcome_label.pack(pady=(20, 30))

    def create_chat_area(self):
        self.chat_area = ChatArea(self.main_container)

        self.chat_area.get_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def create_input_bar(self):
        self.input_bar = InputBar(self.main_container)

        self.input_bar.get_widget().pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )