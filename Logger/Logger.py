from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def assistant(self, message):
        pass

    @abstractmethod
    def user(self, message):
        pass

    def code(self, code):
        pass
