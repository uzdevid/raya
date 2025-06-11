from Logger.Logger import Logger


class StdoutLogger(Logger):
    def info(self, message):
        print(message)

    def error(self, message):
        print(message)
