# 🧠 ai_Desk

**AI-powered Desktop Assistant with Voice, Automation, Memory, and Gemini Intelligence**

ai_Desk is a modern desktop AI assistant built with **Python + CustomTkinter**. It combines **real voice input, Windows automation, conversational AI, persistent memory, and a premium desktop interface** into a single modular application.

![Version](https://img.shields.io/badge/version-v1.3-blue)
![Python](https://img.shields.io/badge/python-3.14+-green)
![Platform](https://img.shields.io/badge/platform-Windows-0078D4)
![Status](https://img.shields.io/badge/status-stable-success)

---

## 🚀 Current Release — v1.3 “AI Brain Online”

### ✨ Working Features

* 🎤 **Real Whisper voice input**
* 🤖 **Official Google Gemini SDK integration**
* 🖥️ **Windows application automation**
* 🌐 **Website launcher**
* 📁 **Folder automation**
* 🧠 **Persistent memory across sessions**
* 📜 **Command history sidebar**
* 🔁 **Repeat previous action**
* 🎨 **Premium responsive desktop UI**
* ⚡ **Multi-model failover architecture**

---

## 🖼️ Interface

The application uses a **dark glassmorphism-inspired UI** with:

* Premium header
* AI status indicator
* Scrollable conversation area
* Touch-friendly input bar
* Voice activation button
* History replay panel

---

## 🎯 Example Commands

### AI Questions

```text
what is java
explain recursion in simple words
what is binary search
```

### Desktop Automation

```text
open calculator
open vscode
open notepad
open terminal
```

### Web & Folders

```text
open github
open youtube
open downloads
open desktop
```

### Memory

```text
open it again
repeat last action
```

---

## 🏗️ Architecture

```text
ai_Desk/
│
├── app/
│   ├── ai/           # Gemini + AI routing
│   ├── voice/        # Whisper voice input
│   ├── memory/       # Persistent memory
│   ├── system/       # Windows automation
│   ├── ui/           # CustomTkinter interface
│   └── core/         # Application bootstrap
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 AI Pipeline

```text
Voice
  ↓
Whisper
  ↓
Message Manager
  ↓
AI Engine
  ↓
Local Memory
  ↓
Gemini SDK
  ↓
Response + Action
```

This design allows ai_Desk to support **voice conversation, desktop control, contextual memory, and cloud AI reasoning**.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhimehra88/ai_Desk.git
cd ai_Desk
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate

**Windows PowerShell**

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run

```bash
python main.py
```

---

## 🧪 Technology Stack

| Layer           | Technology             |
| --------------- | ---------------------- |
| UI              | CustomTkinter          |
| Voice STT       | Faster-Whisper         |
| AI              | Google Gemini SDK      |
| Automation      | Python + Windows APIs  |
| Memory          | JSON-based persistence |
| Version Control | Git & GitHub           |

---

## 📌 Technical Highlights

* **Modular architecture**
* **Separation of UI and business logic**
* **Conversation memory**
* **Voice-to-action workflow**
* **Graceful AI error handling**
* **Responsive layout foundation**
* **Public release tagging workflow**

---

## 🔮 Roadmap

### v1.4 — Reliability & Research

* Web search integration
* Source-aware answers
* Better retry strategy
* Automated testing
* Crash-safe logging

### v1.5 — IRIS Foundation

* Wake word detection
* Background tray service
* Multi-agent workflows
* Local LLM support
* Cross-platform packaging

---

## 👨‍💻 Author

**Abhi Mehra**

* GitHub: https://github.com/abhimehra88

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Why this project matters

ai_Desk is not just a chat application. It is a **voice-enabled AI operating layer** that combines **automation, memory, and conversational intelligence** into a real desktop workflow system.

**Current Status:** ✅ Stable demo-ready release
