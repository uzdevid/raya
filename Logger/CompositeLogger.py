from typing_extensions import override

from Logger.Logger import Logger


class CompositeLogger(Logger):
    def __init__(self, loggers: list):
        self.loggers = loggers

    @override
    def assistant(self, message):
        for logger in self.loggers:
            logger.assistant(message)

    @override
    def user(self, message):
        for logger in self.loggers:
            logger.user(message)

    @override
    def code(self, code):
        for logger in self.loggers:
            logger.code(code)

    def info(self, message):
        for logger in self.loggers:
            logger.info(message)

    def error(self, message):
        for logger in self.loggers:
            logger.error(message)
