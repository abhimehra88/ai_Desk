import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from pathlib import Path
import tempfile


class VoiceInput:

    def __init__(self):
        print("Voice Input Initialized")

        # Load Whisper model
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def listen(self, duration=4):

        sample_rate = 16000

        # Record audio
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.int16
        )

        sd.wait()

        # Save temporary WAV file
        temp_file = Path(tempfile.gettempdir()) / "ai_desk_voice.wav"

        write(temp_file, sample_rate, audio)

        # Transcribe
        segments, _ = self.model.transcribe(str(temp_file))

        text = " ".join(segment.text for segment in segments)

        return text.strip()