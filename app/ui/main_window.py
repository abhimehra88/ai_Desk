import customtkinter as ctk

from app.ui.chat_area import ChatArea
from app.ui.input_bar import InputBar
from app.ui.components.header import Header
from app.system.message_manager import MessageManager


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
        self.header = Header(self.main_container)

    def create_chat_area(self):
        self.chat_area = ChatArea(self.main_container)
        print("MainWindow ChatArea ID:", id(self.chat_area))

        self.chat_area.get_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def create_input_bar(self):

        self.message_manager = MessageManager(self.chat_area)
        
        self.input_bar = InputBar(self.main_container)

        self.input_bar.set_message_manager(self.message_manager)

        self.input_bar.get_widget().pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

