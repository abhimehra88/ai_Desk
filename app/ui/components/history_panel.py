import customtkinter as ctk


class HistoryPanel(ctk.CTkFrame):

    def __init__(self, parent, on_command_click=None):
        super().__init__(parent, width=220, corner_radius=12)

        self.on_command_click = on_command_click
        self.command_buttons = []

        self.pack_propagate(False)

        self.title_label = ctk.CTkLabel(
            self,
            text="🕘 Recent Commands",
            font=(None, 16, "bold")
        )
        self.title_label.pack(pady=(15, 10))

        self.commands_container = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.commands_container.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def update_history(self, commands):

        # Remove old buttons
        for button in self.command_buttons:
            button.destroy()

        self.command_buttons.clear()

        # Show newest first
        for command in reversed(commands):

            button = ctk.CTkButton(
                self.commands_container,
                text=command,
                anchor="w",
                height=36,
                fg_color="#2B2B2B",
                hover_color="#3A3A3A",
                command=lambda cmd=command: self.handle_click(cmd)
            )

            button.pack(fill="x", pady=4)

            self.command_buttons.append(button)

    def handle_click(self, command):

        if self.on_command_click:
            self.on_command_click(command)