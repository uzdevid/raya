from Logger.MemoryLogger import MemoryLogger
from Logger.FileLogger import FileLogger
from Logger.Logger import Logger


class CompositeLogger(Logger):
    def __init__(self, fileLogger: FileLogger, memoryLogger: MemoryLogger):
        self.file = fileLogger
        self.memory = memoryLogger

    def assistant(self, message):
        self.file.assistant(message)
        self.memory.assistant(message)

    def user(self, message):
        self.file.user(message)
        self.memory.user(message)

    def code(self, code):
        self.file.code(code)
        self.memory.code(code)
