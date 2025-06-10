import re

import numpy as np
import sounddevice as sd
import torch


class Output:
    def __init__(self):
        model, example = torch.hub.load(
            repo_or_dir='snakers4/silero-models',
            model='silero_tts',
            language='ru',
            speaker='v4_ru'
        )

        device = "cuda:0" if torch.cuda.is_available() else "cpu"

        model.to(torch.device(device))

        self.model = model

    @staticmethod
    def print(text: str):
        print(text)

    def speak(self, text: str):
        if len(text) <= 1000:
            return self.__speak(text)

        parts = self.__splitText(text)
        for part in parts:
            if len(part) > 0:
                self.__speak(part)

    def __speak(self, text: str):
        audio = self.model.apply_tts(text=text, speaker='xenia', sample_rate=48000)

        audio_np = np.array(audio).reshape(-1, 1)

        sd.play(audio_np, samplerate=48000)
        sd.wait()

    @staticmethod
    def __cleanString(text: str):
        return re.sub(r'[^a-zA-Zа-яА-Я0-9.,!?;:(){}[\]<>-]', '', text)

    @staticmethod
    def __splitText(text: str) -> list:
        parts = []
        while len(text) > 1000:
            # Ищем последнее предложение до max_len
            split_idx = text.rfind('.', 0, 1000)
            if split_idx == -1:
                split_idx = 1000  # не нашли точку — просто обрежем
            part = text[:split_idx + 1].strip()
            parts.append(part)
            text = text[split_idx + 1:].strip()
        if text:
            parts.append(text)
        return parts
