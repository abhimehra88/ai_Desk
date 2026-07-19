import os
import shutil
import subprocess

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
                path = path.format(os.getlogin())

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