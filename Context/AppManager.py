import json
import os

from Context.CtxModule import CtxModule


class AppManager(CtxModule):
    def run(self, name: str):
        with open('./Context/apps.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        name_query = name.lower()
        for program in data:
            if any(name_query in name.lower() for name in program['names']):
                self.ctx.ui.speak(f"Запускаю: {program['name']}")
                os.startfile(program['path'])
                return

        self.ctx.ui.speak(f"Программа: {name} не найдена.")
