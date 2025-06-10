from abc import ABC, abstractmethod


class Input(ABC):
    @abstractmethod
    def getPrompt(self, message: str = None):
        pass
