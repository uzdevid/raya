import datetime
import os

from Logger.Logger import Logger


class FileLogger(Logger):
    def __init__(self, filename: str):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                pass

    def _write(self, level, message):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{now}] [{level.upper()}] {message}"
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(log_line + '\n')

    def info(self, message):
        self._write('info', message)

    def error(self, message):
        self._write('error', message)
