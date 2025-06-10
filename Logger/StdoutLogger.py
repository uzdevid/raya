from Logger.Logger import Logger


class StdoutLogger(Logger):
    def assistant(self, message):
        self._write('assistant', message)

    def user(self, message):
        self._write('user', message)

    def code(self, code):
        self._write('code', code)

    @staticmethod
    def _write(role, message):
        print(role, ': ', message)
