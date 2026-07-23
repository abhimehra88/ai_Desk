import threading
import time
from app.ai.ai_engine import AIEngine


class MessageManager:

    def __init__(self, chat_area, main_window=None):

        self.chat_area = chat_area
        self.main_window = main_window
        self.ai_engine = AIEngine()

        self.is_generating = False
        self.current_stream_label = None

        # Welcome message
        self.send_ai_message("Hello! I am ready to help you.")

    # =====================================================
    # USER MESSAGE ENTRY POINT
    # =====================================================

    def send_user_message(self, message):

        if not message or not message.strip():
            return

        # Prevent multiple generations
        if self.is_generating:
            self.send_system_message(
                "⏳ Please wait, I am still generating a response."
            )
            return

        self.is_generating = True

        # 1. Show user message instantly
        self.chat_area.add_message("You", message)

        # 2. Create editable thinking bubble
        self.current_stream_label = self.chat_area.add_message(
            "ai_Desk",
            "🧠 ai_Desk is thinking..."
        )

        # 3. Run AI in background
        thread = threading.Thread(
            target=self._generate_reply,
            args=(message,),
            daemon=True
        )

        thread.start()

    # =====================================================
    # BACKGROUND AI WORK
    # =====================================================

    def _handle_stream_error(self, error_text):

        print(f"[STREAM FAILSAFE] {error_text}")

        try:

            # Replace thinking bubble with error
            if self.current_stream_lable:
                self.current_stream_label.configure(
                    text=f"⚠️ Streaming error: {error_text}"
                )
        except Exception:
            pass

        # CRITICAL: always reset state
        self.current_stream_label = None
        self.is_generating = False

    def _generate_reply(self, message):

        try:

            reply = self.ai_engine.generate_response(message)

            # Start streaming on main thread
            self.chat_area.get_widget().after(
                0,
                lambda: self._stream_reply(reply)
            )

        except Exception as error:

            print(f"[STREAM ERROR] {error}")

            self.chat_area.get_widget().after(
                0,
                lambda: self._handle_stream_error(str(error))
            )


    # =====================================================
    # STREAMING EFFECT
    # =====================================================

    def _stream_reply(self, full_text):

        if not self.current_stream_label:
            self._finish_generation(full_text)
            return

        # Clear thinking text
        self.current_stream_label.configure(text="")

        chunks = full_text.split(" ")
        current = ""

        self._stream_chunks(chunks, current, 0)

    def _stream_chunks(self, chunks, current_text, index):

        try:

            # Streaming finished
            if index >= len(chunks):
                self._finish_streaming()
                return

            # Add next word
            current_text += chunks[index] + " "

            # Update bubble safety
            if self.current_stream_label:
                self.current_stream_label.configure(text=current_text.strip())

            try:
                # Auto scroll
                self.chat_area.chat_box._parent_canvas.yview_moveto(1.0)
            except Exception:
                pass

            # Schedule next chunk
            self.chat_area.get_widget().after(
                20,  # milliseconds between updates
                lambda: self._stream_chunks(chunks, current_text, index + 1)
            )

        except Exception as error:

            print(f"[STREAM LOOP ERROR] {error}")

            # Never leave the app stuck
            self._handle_stream_error(str(error))

    # =====================================================
    # FINISH STREAMING
    # =====================================================

    def _finish_streaming(self):

        # Developer log
        if self.current_stream_label:
            try:
                final_text = self.current_stream_label.cget("text")
                print(f">>>  🤖 ai_Desk: {final_text}")
            except Exception:
                pass

        # Update history sidebar
        if self.main_window:
            recent_commands = self.ai_engine.get_recent_commands()
            self.main_window.history_panel.update_history(recent_commands)

        self.current_stream_label = None
        self.is_generating = False

    # =====================================================
    # ERROR / DIRECT FINISH
    # =====================================================

    def _finish_generation(self, message):

        if self.current_stream_label:
            self.current_stream_label.configure(text=message)
        else:
            self.send_ai_message(message)

        self._finish_streaming()

    # =====================================================
    # BASIC HELPERS
    # =====================================================

    def send_ai_message(self, message):
        return self.chat_area.add_message("ai_Desk", message)

    def send_system_message(self, message):
        return self.chat_area.add_message("System", message)