from Logger.Logger import Logger


class CompositeLogger(Logger):
    def __init__(self, loggers: list):
        self.loggers = loggers

    def assistant(self, message):
        for logger in self.loggers:
            logger.assistant(message)

    def user(self, message):
        for logger in self.loggers:
            logger.user(message)

    def code(self, code):
        for logger in self.loggers:
            logger.code(code)
