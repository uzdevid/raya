from abc import ABC, abstractmethod

from Core.UserInterface import UserInterface


class AbstractDispatcher(ABC):
    @abstractmethod
    def getAliases(self) -> list:
        pass

    @abstractmethod
    def start(self, ui: UserInterface):
        pass
