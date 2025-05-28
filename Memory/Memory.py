from abc import ABC, abstractmethod


class Memory(ABC):
    @abstractmethod
    def save(self, role, message):
        pass

    @abstractmethod
    def remember(self, text):
        pass

    def getHistory(self) -> list:
        pass
