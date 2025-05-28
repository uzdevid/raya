import json
from datetime import datetime

from Memory.Memory import Memory


class JsonMemory(Memory):
    def __init__(self):
        self.filename = './Memory/raya.json'

    def save(self, role, message):
        self._write(role, message)

    def remember(self, text):
        self._write('remember', text)

    def getHistory(self) -> list:
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write(self, role, message):
        now = datetime.now().isoformat()

        new_entry = {'timestamp': now, 'role': role, 'message': message}

        with open(self.filename, 'r', encoding='utf-8') as f:
            try:
                log_data = json.load(f)
            except json.JSONDecodeError:
                log_data = []

        log_data.append(new_entry)

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
