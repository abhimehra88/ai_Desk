import customtkinter as ctk
from app.ui.main_window import MainWindow


class Application:

    def __init__(self):

        print("Application Started")

        # Global theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        # Window
        self.root.title("ai_Desk — AI Brain Online")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 700)

        # Premium dark background
        self.root.configure(fg_color="#0B1020")

        MainWindow(self.root)

    def run(self):
        self.root.mainloop()