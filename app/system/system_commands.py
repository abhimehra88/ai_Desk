import subprocess


class SystemCommands:

    def __init__(self):
        print("System Commands Loaded")

        self.apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
        }

    def execute(self, command):

        command = command.lower().strip()

        if command.startswith("open "):

            app_name = command.replace("open", "").strip()
            
            if app_name in self.apps:
                    subprocess.Popen(self.apps[app_name])
                    return f"Opening {app_name.title()}..."

            return f"I don't know how to open '{app_name}'."
    
        return "Unkown system command"

    