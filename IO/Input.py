import speech_recognition as sr

from speech_recognition import Recognizer

class Input:
    engine: Recognizer
    language: str

    def __init__(self, language: str):
        self.language = language
        self.engine = sr.Recognizer()

        self.microphone = sr.Microphone(device_index=1)

        self.engine.pause_threshold = 0.8
        self.engine.energy_threshold = 200
        self.engine.dynamic_energy_threshold = True


    def get(self, inputPrompt: str = 'Prompt'):
        return self.text()

    def text(self, inputPrompt: str = 'Prompt'):
        return input(f"{inputPrompt}: ")

    def audio(self):
        with self.microphone as source:
            self.engine.adjust_for_ambient_noise(source)
            voice = self.engine.listen(source)

        try:
            return self.engine.recognize_google(voice, language=self.language).lower().strip()
        except sr.UnknownValueError:
            return self.audio()