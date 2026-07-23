from datetime import datetime

from app.system.system_commands import SystemCommands
from app.memory.memory_manager import MemoryManager
from app.ai.llm_client import LLMClient
from app.ai.local_knowledge import LOCAL_KNOWLEDGE
from app.research.web_search import WebSearch
from app.research.summarizer import SearchSummarizer
from app.ai.response_formatter import ResponseFormatter
from app.ai.question_splitter import QuestionSplitter


class AIEngine:

    def __init__(self):
        print("AI Engine Initialized")

        self.system = SystemCommands()
        self.memory = MemoryManager()
        self.llm = LLMClient()

        # Remember last live-search topic
        self.last_live_topic = None

    # =====================================================
    # MAIN ENTRY
    # =====================================================

    def generate_response(self, message):

        original_message = message.strip()
        normalized_message = original_message.lower().strip()

        # Save history
        self.memory.add_recent_command(original_message)

        # =====================================================
        # SAFE AUTOMATION (ONLY PURE COMMANDS)
        # =====================================================

        if self.is_pure_command(normalized_message):

            # App launch
            app_name = self.system.extract_app_name(normalized_message)

            if app_name:
                success, response = self.system.open_app(app_name)

                if success:
                    self.memory.set_last_action(normalized_message)

                return response

            # Website
            success, response = self.system.open_website(normalized_message)

            if success:
                self.memory.set_last_action(normalized_message)
                return response

            # Folder
            success, response = self.system.open_folder(normalized_message)

            if success:
                self.memory.set_last_action(normalized_message)
                return response

        # =====================================================
        # INTENT SYSTEM
        # =====================================================

        intent = self.detect_intent(normalized_message)

        return self.handle_intent(intent, original_message)

    # =====================================================
    # PURE COMMAND DETECTION
    # =====================================================

    def is_pure_command(self, message):

        text = message.strip()

        # Multi-line message = not a command
        if "\n" in text:
            return False

        command_starts = (
            "open ",
            "launch ",
            "start "
        )

        if not text.startswith(command_starts):
            return False

        # Too many words = probably a question
        if len(text.split()) > 5:
            return False

        return True

    # =====================================================
    # LIVE SEARCH DETECTION
    # =====================================================

    def needs_live_search(self, message):

        # Ignore internal prompts
        if message.startswith("User searched for:"):
            return False

        if message.startswith("Live web search results:"):
            return False

        if "Using these live web results" in message:
            return False

        text = message.lower()

        # Direct live keywords
        keywords = [
            "latest",
            "current",
            "today",
            "yesterday",
            "news",
            "live",
            "breaking",
            "score",
            "result",
            "winner",
            "match",
            "weather",
            "stock",
            "price",
            "fifa",
            "world cup",
            "final",
            "won",
            "bitcoin",
            "ceo"
        ]

        if any(keyword in text for keyword in keywords):
            return True

        # Follow-up queries after a live topic
        follow_up_starts = (
            "and ",
            "what about",
            "who scored",
            "what was the score",
            "what happened",
            "is it true",
            "really",
            "then why"
        )

        if self.last_live_topic and text.startswith(follow_up_starts):
            return True

        return False

    # =====================================================
    # INTENT DETECTION
    # =====================================================

    def detect_intent(self, message):

        greetings = ["hi", "hello", "hey"]

        if message in greetings:
            return "greeting"

        if "time" in message:
            return "time"

        if "date" in message:
            return "date"

        if message in ["who are you", "about yourself"]:
            return "identity"

        repeat_phrases = [
            "open it again",
            "repeat last action",
            "do it again",
            "repeat previous command"
        ]

        if message in repeat_phrases:
            return "repeat"

        if message in ["continue", "next", "more"]:
            return "continue_lesson"

        return "unknown"

    # =====================================================
    # INTENT HANDLER
    # =====================================================

    def handle_intent(self, intent, message):

        if intent == "greeting":
            return self.handle_greetings()

        if intent == "time":
            return self.handle_time()

        if intent == "date":
            return self.handle_date()

        if intent == "identity":
            return self.handle_identity()

        if intent == "repeat":
            return self.handle_repeat()

        multi_answer = self.handle_multi_question(message)

        if multi_answer:
            return multi_answer
        
        return self.handle_fallback(message)
    # =====================================================
    # REPEAT ACTION
    # =====================================================

    def handle_repeat(self):

        last_action = self.memory.get_last_action()

        if not last_action:
            return "I don't have any previous action to repeat."

        # Try app
        app_name = self.system.extract_app_name(last_action)

        if app_name:
            success, response = self.system.open_app(app_name)

            if success:
                return f"Repeating previous action: {response}"

        # Try website
        success, response = self.system.open_website(last_action)

        if success:
            return f"Repeating previous action: {response}"

        # Try folder
        success, response = self.system.open_folder(last_action)

        if success:
            return f"Repeating previous action: {response}"

        return "I couldn't repeat the previous action."

    # =====================================================
    # BASIC RESPONSES
    # =====================================================

    def handle_greetings(self):
        return "Hello! How can I help you today?"

    def handle_time(self):
        return datetime.now().strftime("%I:%M %p")

    def handle_date(self):
        return datetime.now().strftime("%d %B %Y")

    def handle_identity(self):
        return "I am ai_Desk, your intelligent desktop assistant."

    # =====================================================
    # AI + WEB FALLBACK
    # =====================================================

    def handle_multi_question(self, message):

        questions = QuestionSplitter.split(message)

        # Single question → Normal flow
        if len(questions) == 1:
            return None
        
        answers = []

        for index, question in enumerate(questions, start=1):

            # Use the existing fallback logic for each question
            answer = self.handle_fallback(question)

            answers.append(
                f"**{index}. {question}**\n{answer}"
            )

        return "\n\n---\n\n".join(answers)

    def handle_fallback(self, message):

        # =====================================================
        # LIVE WEB SEARCH
        # =====================================================

        if self.needs_live_search(message):

            print(f"[WEB] Searching: {message}")

            self.last_live_topic = message

            search_data = WebSearch.search(message)

            if search_data["success"] and search_data["results"]:

                context = SearchSummarizer.build_context(search_data)

                if context:

                    # IMPORTANT: send CONTEXT, not original message
                    raw = self.llm.generate(context)

                    cleaned = ResponseFormatter.clean(raw)

                    return ResponseFormatter.make_human(
                        message,
                        cleaned
                    )

                return "I found live web results but could not summarize them."

            return (
                "⚠️ I couldn't fetch live web results right now. "
                "Please check your internet connection and try again."
            )

        # =====================================================
        # NORMAL AI
        # =====================================================

        raw = self.llm.generate(message)

        cleaned = ResponseFormatter.clean(raw)

        return ResponseFormatter.make_human(message, cleaned)

    # =====================================================
    # HISTORY
    # =====================================================

    def get_recent_commands(self):
        return self.memory.get_recent_commands()