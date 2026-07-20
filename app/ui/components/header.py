import customtkinter as ctk
from datetime import datetime


class Header:

    def __init__(self, parent):
        self.parent = parent
        self.widget = self.create()

    def create(self):

        # Main glass card
        frame = ctk.CTkFrame(
            self.parent,
            height=88,
            corner_radius=24,
            fg_color="#0F172A",
            border_width=1,
            border_color="#1E293B"
        )

        frame.pack_propagate(False)

        # LEFT SECTION
        left = ctk.CTkFrame(frame, fg_color="transparent")
        left.pack(side="left", fill="y", padx=20, pady=14)

        # Logo + Title row
        title_row = ctk.CTkFrame(left, fg_color="transparent")
        title_row.pack(anchor="w")

        logo = ctk.CTkLabel(
            title_row,
            text="🧠",
            font=ctk.CTkFont(size=30)
        )
        logo.pack(side="left", padx=(0, 10))

        title = ctk.CTkLabel(
            title_row,
            text="ai_Desk",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#F8FAFC"
        )
        title.pack(side="left")

        subtitle = ctk.CTkLabel(
            left,
            text="Voice • Automation • Gemini AI • Memory",
            font=ctk.CTkFont(size=12),
            text_color="#94A3B8"
        )
        subtitle.pack(anchor="w", pady=(4, 0))

        # RIGHT SECTION
        right = ctk.CTkFrame(frame, fg_color="transparent")
        right.pack(side="right", fill="y", padx=20, pady=14)

        # Status pill
        status_frame = ctk.CTkFrame(
            right,
            corner_radius=999,
            fg_color="#10251B",
            border_width=1,
            border_color="#1F8A5B"
        )
        status_frame.pack(anchor="e")

        status_label = ctk.CTkLabel(
            status_frame,
            text="● AI ONLINE",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#22C55E",
            padx=14,
            pady=6
        )
        status_label.pack()

        # Time
        time_label = ctk.CTkLabel(
            right,
            text=datetime.now().strftime("%d %b %Y • %I:%M %p"),
            font=ctk.CTkFont(size=11),
            text_color="#64748B"
        )
        time_label.pack(anchor="e", pady=(10, 0))

        return frame

    def get_widget(self):
        return self.widget