import customtkinter as ctk

from app.ui.chat_area import ChatArea
from app.ui.input_bar import InputBar
from app.ui.components.header import Header
from app.system.message_manager import MessageManager
from app.ui.components.history_panel import HistoryPanel


class MainWindow:
    def __init__(self, root):
        self.root = root

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.is_mobile = self.screen_width <700

        print(f"Screen: {self.screen_width}x{self.screen_height}")
        print(f"Mobile mode: {self.is_mobile}")

        self.build_ui()

    def build_ui(self):
        self.create_main_container()
        self.create_header()
        self.create_chat_area()
        self.create_input_bar()

    def create_main_container(self):

        # Main wrapper
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

        # LEFT HISTORY PANEL
        self.history_panel = HistoryPanel(
            self.main_container,
            on_command_click = self.on_history_command_click
        )

        self.history_panel.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        # RIGHT CONTENT AREA    
        self.content_frame = ctk.CTkFrame(
            self.main_container,
            fg_color="transparent"
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )


    def create_header(self):
        self.header = Header(self.content_frame)

        self.header.get_widget().pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

    def create_chat_area(self):
        self.chat_area = ChatArea(self.content_frame)
        print("MainWindow ChatArea ID:", id(self.chat_area))

        self.chat_area.get_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

    def create_input_bar(self):

        self.message_manager = MessageManager(
            self.chat_area,
            self
        )
        
        self.input_bar = InputBar(self.content_frame)

        self.input_bar.set_message_manager(self.message_manager)

        self.input_bar.get_widget().pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

    def update_history(self, commands):
        self.history_panel.update_history(commands)

    def on_history_command_click(self, command):

        # Clear textbox
        self.input_bar.entry.delete("1.0", "end")

        # Insert selected comand
        self.input_bar.entry.insert("1.0", command)

        # Foocus textbox
        self.input_bar.entry.focus()
        

