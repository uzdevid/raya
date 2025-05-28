from abc import ABC, abstractmethod

from Core.UserInterface import UserInterface


class AbstractDispatcher(ABC):
    @abstractmethod
    def getApiKey(self) -> str:
        pass

    @abstractmethod
    def getModel(self) -> str:
        pass

    @abstractmethod
    def start(self, ui: UserInterface):
        pass
