import json
from pathlib import Path


class MemoryManager:

    def __init__(self):
        self.memory_file = Path(__file__).parent / "memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {
                "user_name": None,
                "last_action": None,
                "recent_commands": []
            }

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(self.memory, file, indent=4)

    def set_last_action(self, action):
        self.memory["last_action"] = action
        self.save_memory()

    def get_last_action(self):
        return self.memory.get("last_action")

    def add_recent_command(self, command):
        commands = self.memory["recent_commands"]
        commands.append(command)

        # Keep only last 10 commands
        self.memory["recent_commands"] = commands[-10:]

        self.save_memory()

    def get_recent_commands(self):
        return self.memory.get("recent_commands", [])