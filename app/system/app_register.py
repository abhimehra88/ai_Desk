# app/system/app_register.py

APP_REGISTRY = {
    # Windows built-in apps
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "paint": ["mspaint.exe"],
    "cmd": ["cmd.exe"],

    # Google Chrome
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "chrome.exe"
    ],

    # Visual Studio Code
    "vscode": [
        r"D:\Microsoft VS Code\Code.exe",
        r"D:\Microsoft VS Code\bin\code",
        r"D:\Microsoft VS Code\bin\code.cmd",
        "code",
        "code.cmd",
        "code.exe"
    ]
}

# Natural language aliases
APP_ALIASES = {
    # Chrome
    "chrome": "chrome",
    "google chrome": "chrome",
    "browser": "chrome",

    # VS Code
    "vscode": "vscode",
    "vs code": "vscode",
    "visual studio code": "vscode",
    "code editor": "vscode",

    # Existing apps
    "notepad": "notepad",
    "calculator": "calculator",
    "paint": "paint",
    "cmd": "cmd"
}