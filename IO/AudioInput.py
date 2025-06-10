import speech_recognition as sr
from speech_recognition import Recognizer

from IO.Input import Input


class AudioInput(Input):
    engine: Recognizer
    language: str

    def __init__(self, language: str):
        self.language = language
        self.engine = sr.Recognizer()

        self.microphone = sr.Microphone(device_index=1)

        self.engine.pause_threshold = 0.8
        self.engine.energy_threshold = 200
        self.engine.dynamic_energy_threshold = True

    def getPrompt(self, message: str = None):
        with self.microphone as source:
            self.engine.adjust_for_ambient_noise(source)
            voice = self.engine.listen(source)

        try:
            return self.engine.recognize_google(voice, language=self.language).lower().strip()
        except sr.UnknownValueError:
            return self.getPrompt()
