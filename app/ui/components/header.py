import customtkinter as ctk


class Header:

    def __init__(self, parent):
        self.parent = parent
        self.widget = self.create_header()

    def create_header(self):

        frame = ctk.CTkFrame(
            self.parent,
            height=70,
            corner_radius=15
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        frame.pack_propagate(False)

        title = ctk.CTkLabel(
            frame,
            text="🤖 ai_Desk",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(
            side="left",
            padx=20
        )

        status = ctk.CTkLabel(
            frame,
            text="🟢 Online",
            font=("Segoe UI", 14)
        )

        status.pack(
            side="right",
            padx=20
        )

        return frame

    def get_widget(self):
        return self.widget