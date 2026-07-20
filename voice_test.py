from app.voice.voice_input import VoiceInput

voice = VoiceInput()

print("Speak now...")

text = voice.listen()

print(f"You said: {text}")