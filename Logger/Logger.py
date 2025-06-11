from abc import ABC, abstractmethod


class Logger(ABC):
    def assistant(self, message):
        self.info('Assistant:' + message)

    def user(self, message):
        self.info('User:' + message)

    def code(self, code):
        self.info('Code:' + code)

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass
