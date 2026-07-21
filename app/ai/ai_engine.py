from datetime import datetime
from app.system.system_commands import SystemCommands
from app.memory.memory_manager import MemoryManager 
from app.ai.llm_client import LLMClient
from app.ai.local_knowledge import LOCAL_KNOWLEDGE
from app.research.web_search import WebSearch
from app.research.summarizer import SearchSummarizer


class AIEngine:

    def __init__(self):
        print("AI Engine Initialized")

        self.system = SystemCommands()
        self.memory = MemoryManager()
        self.llm = LLMClient()


    def generate_response(self, message):

        message = message.lower().strip()
        self.memory.add_recent_command(message)


        # =========================
        # APP LAUNCH HANDLER
        # =========================
        app_name = self.system.extract_app_name(message)

        if app_name:
            success, response = self.system.open_app(app_name)

            if success:
                self.memory.set_last_action (message)

            return response
        
        # =========================
        # WEBSITE HANDLER
        # =========================
        success, response = self.system.open_website(message)

        if success:
            self.memory.set_last_action(message)

            return response
        
        # =========================
        # FOLDER HANDLER
        # =========================
        success, response = self.system.open_folder(message)

        if success:
            return response

        # =========================
        # EXISTING INTENT SYSTEM
        # =========================
        intent = self.detect_intent(message)

        return self.handle_intent(intent, message)
    
    def needs_live_search(self, message):

        # Ignore internal system prompts
        if message.startswith("User searched for:"):
            return False
        
        if message.startswith("Live web search results:"):
            return False
        
        if "Using these live web results" in message:
            return False

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
            "price"
            "fifa",
            "world cup",
            "final",
            "won"
        ]

        message = message.lower()

        return any(keyword in message for keyword in keywords)

    def detect_intent(self, message):

        if message in ["hi", "hello", "hey"]:
            return "greeting"

        if "time" in message:
            return "time"

        if "date" in message:
            return "date"

        if message in ["who are you", "about yourself"]:
            return "identity"
        
        if message in [
            "open it again",
            "repeat last action",
            "do it again",
            "repeat previous command"
        ]:
            return "repeat"

        if message.startswith("open "):
            return "system"

        return "unknown"

    def handle_intent(self, intent, message):

        if intent == "greeting":
            return self.handle_greetings()

        if intent == "time":
            return self.handle_time()

        if intent == "date":
            return self.handle_date()

        if intent == "identity":
            return self.handle_identity()

        if intent == "system":
            self.memory.set_last_action(message)
            
            app_name = self.system.extract_app_name(message)

            if app_name:
                success, response = self.system.open_app(app_name)
                return response
            
            return "I couldn't understand which application to open."
        
        if intent == "repeat":

            last_action = self.memory.get_last_action()

            if last_action:
               
               # Try app first
               app_name =  self.system.extract_app_name(last_action)

               if app_name:
                    success, response = self.system.open_app(app_name)

                    if success:
                        return f"Repeating previous action: {response}"
                    
                    
                    # Try website 
                    success, response = self.system.open_website(last_action)

                    if success:
                        return f"Repeating previous action: {response}"
            
                    return "I couldn't repeat the previous action."
               
               return "I don't have any previous action to repeat."
            
        return self.handle_fallback(message)

        
    def handle_greetings(self):
        return "Hello! How can I help you today?"

    def handle_time(self):
        return datetime.now().strftime("%I:%M %p")

    def handle_date(self):
        return datetime.now().strftime("%d %B %Y")

    def handle_identity(self):
        return "I am ai_Desk, your intelligent desktop assistant."

    def handle_fallback(self, message):

        # =========================
        # LIVE WEB SEARCH
        # =========================
        if self.needs_live_search(message):

            print(f"[WEB] Searching: {message}")

            search_data = WebSearch.search(message)

            if search_data["success"] and search_data["results"]:
                context = SearchSummarizer.build_context(search_data)

                if context:
                    return self.llm.generate(context)
                
                return "I found live web results but could not summarize them."
            
            return "I could not fetch live web results right now."
        
        # =========================
        # NORMAL AI
        # =========================
        return self.llm.generate(message)

    
    def get_recent_commands(self):
        return self.memory.get_recent_commands()