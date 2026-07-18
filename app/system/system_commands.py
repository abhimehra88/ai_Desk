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
        

        if "open" in command:

            app_name = self.extract_app_name(command)
            
            if app_name in self.apps:
                    subprocess.Popen(self.apps[app_name])
                    return f"Opening {app_name.title()}..."

            return f"I don't know how to open '{app_name}'."
    
        return "Unkown system command"
    
    def extract_app_name(self, command):
         
         words = command.lower().split()

         remove_words = [
              "can",
              "you",
              "please",
              "open",
              "the",
              "app",
              "application"
         ]
         
         app_words = []

         for word in words:
              if word not in remove_words:
                   app_words.append(word)

         return " ".join(app_words).strip()

    