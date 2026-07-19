# app/system/app_register.py

APP_REGISTRY = {
    # Windows built-in apps
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "paint": ["mspaint.exe"],
    "cmd": ["cmd.exe"],
    "terminal": ["wt.exe", "cmd.exe"],

    # Google Chrome
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "chrome.exe"
    ],

    # Visual Studio Code
    # Visual Studio Code
    "vscode": [
        r"D:\Microsoft VS Code\Code.exe",
        r"D:\Microsoft VS Code\bin\code",
        r"D:\Microsoft VS Code\bin\code.cmd",
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
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

    # Notepad
    "notepad": "notepad",

    # Calculator
    "calculator": "calculator",
    "calc": "calculator",

    # Paint
    "paint": "paint",

    # Terminal
    "cmd": "cmd",
    "terminal": "cmd",
    "terminal": "terminal",
    "windows terminal": "terminal",
    "command prompt": "cmd",
}