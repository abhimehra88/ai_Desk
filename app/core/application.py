from app.ui.main_window import MainWindow
import customtkinter as ctk


class Application:
    def __init__(self):
        print("Application Started")
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Create main window
        self.root = ctk.CTk()
        self.root.title("ai_Desk")
        #self.root.configure(fg_color="system")
        self.root.geometry("1200x700")
        
        MainWindow(self.root)

    def run(self):
        self.root.mainloop()