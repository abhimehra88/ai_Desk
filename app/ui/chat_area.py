import customtkinter as ctk


class ChatArea:

    def __init__(self, parent):
        self.parent = parent
        self.widget = self.create()

    def create(self):

        # Outer glass card
        self.frame = ctk.CTkFrame(
            self.parent,
            corner_radius=28,
            fg_color="#111827",
            border_width=1,
            border_color="#334155"
        )

        # Scrollable chat
        self.chat_box = ctk.CTkScrollableFrame(
            self.frame,
            fg_color="transparent",
            scrollbar_button_color="#334155",
            scrollbar_button_hover_color="#475569"
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=16,
            pady=16
        )

        return self.frame

    def get_widget(self):
        return self.widget

    def add_message(self, sender, message):

        # Message type detection
        is_user = sender in ["You", "User", "Abhi"]
        is_system = sender in ["System", "⚙️ System"]

        # Row container
        row = ctk.CTkFrame(
            self.chat_box,
            fg_color="transparent"
        )
        row.pack(fill="x", pady=8)

        # Alignment
        if is_user:
            side = "right"
            bubble_color = "#2563EB"  # Blue
            sender_color = "#DBEAFE"
            display_name = "You"

        elif is_system:
            side = "left"
            bubble_color = "#3B2F0B"  # Amber
            sender_color = "#FDE68A"
            display_name = "System"

        else:
            side = "left"
            bubble_color = "#1E293B"  # Slate
            sender_color = "#93C5FD"
            display_name = "ai_Desk"

        # Bubble
        bubble = ctk.CTkFrame(
            row,
            corner_radius=22,
            fg_color=bubble_color,
            border_width=0
        )

        bubble.pack(side=side, padx=4)

        # Sender label
        sender_label = ctk.CTkLabel(
            bubble,
            text=display_name,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=sender_color
        )
        sender_label.pack(anchor="w", padx=14, pady=(10, 2))

        # Message text
        message_label = ctk.CTkLabel(
            bubble,
            text=message,
            font=ctk.CTkFont(size=14),
            text_color="#FFFFFF",
            justify="left",
            wraplength=700
        )
        message_label.pack(anchor="w", padx=14, pady=(0, 12))

        # Auto scroll to bottom
        self.chat_box._parent_canvas.yview_moveto(1.0)

        # Console debug
        icon = "👤" if is_user else ("⚙️" if is_system else "🤖")
        print(f">>> {icon} {display_name}: {message}")

    def clear_chat(self):
        for widget in self.chat_box.winfo_children():
            widget.destroy()