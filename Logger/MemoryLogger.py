from Logger.Logger import Logger
from Memory.Memory import Memory


class MemoryLogger(Logger):
    def __init__(self, memory: Memory):
        self.memory = memory

    def assistant(self, message):
        self._write('assistant', message)

    def user(self, message):
        self._write('user', message)

    def code(self, code):
        self._write('code', code)

    def _write(self, role, message):
        self.memory.save(role, message)
