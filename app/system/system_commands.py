import os
import shutil
import subprocess
import webbrowser

from app.system.app_register import APP_REGISTRY, APP_ALIASES

class SystemCommands:

    @staticmethod
    def find_app(app_name):
        app_name = app_name.lower()

        if app_name not in APP_REGISTRY:
            return None

        candidates = APP_REGISTRY[app_name]

        for path in candidates:

            # username replace
            if "{}" in path:
                username = os.environ.get("USERNAME", "")
                path = path.format(username)

            # full path exists
            if os.path.exists(path):
                return path

            # PATH environment check
            if shutil.which(path):
                return shutil.which(path)

        return None
    
    @staticmethod
    def open_app(app_name):
        app_path = SystemCommands.find_app(app_name)

        if not app_path:
            return False, f"{app_name} not found on this system."

        try:
            if app_name == "cmd":
                subprocess.Popen(["cmd.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(app_path)

            return True, f"Opening {app_name}"
        
        except Exception as e:
            return False, str(e)
        
    @staticmethod
    def extract_app_name(text):
        text = text.lower()

        for alias, app in APP_ALIASES.items():
            if alias in text:
                return app
            
        return None
    
    @staticmethod
    def open_website(text):

        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://github.com",
            "chatgpt": "https://chat.openai.com",
            "linkedin": "https://www.linkedin.com"
        }

        text = text.lower()

        # Only trigger for explicit open commands
        if not text.startswith(("open ", "launch ", "start ")):
            return False, None
        
        for name, url in websites.items():
            if name in text:
                webbrowser.open(url)
                return True, f"Opening {name}"

        return False, None
    
    @staticmethod
    def open_folder(text):

        folders = {
            "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
            "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "pictures": os.path.join(os.path.expanduser("~"), "Pictures")
        }

        text = text.lower().strip()

        if not text.startswith(("open ", "launch ", "start ")):
            return False, None

        for name, path in folders.items():
            if name in text and os.path.exists(path):
                os.startfile(path)
                return True, f"Opening {name}"

        return False, None