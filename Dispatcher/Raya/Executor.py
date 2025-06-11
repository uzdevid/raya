import re

from Context.Ctx import Ctx
from Core.Executor import AbstractExecutor


class Executor(AbstractExecutor):
    def __init__(self, ctx: Ctx):
        self.ctx = ctx

    def execute(self, code: str):
        try:
            exec(self.__clear(code), {}, {'ctx': self.ctx})
        except Exception as e:
            self.ctx.logger.error(str(e))
            self.ctx.ui.speak('Прошу прощения! Получила ошибку при выполнении команды. Детальная информация на экране.')

    @staticmethod
    def __clear(code: str):
        return re.sub(r"^```(?:python)?\n|\n```$", "", code.strip())
