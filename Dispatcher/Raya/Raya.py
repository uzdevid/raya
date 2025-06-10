import os
import time

from Core.Dispatcher import AbstractDispatcher
from Core.Executor import AbstractExecutor
from Core.UserInterface import UserInterface
from Dispatcher.Raya.Handler import Handler
from Logger.Logger import Logger


class Dispatcher(AbstractDispatcher):
    aliases = ['рая']
    lastCall: float = time.time()

    def __init__(self, executor: AbstractExecutor, logger: Logger):
        self.handler = Handler(self.getApiKey(), self.getModel())
        self.executor = executor
        self.logger = logger

    def getApiKey(self) -> str:
        return os.getenv("OPENAI_API_KEY")

    def getModel(self) -> str:
        return 'gpt-4-turbo'

    def start(self, ui: UserInterface):
        prompt = ui.input.getPrompt()

        for alias in self.aliases:
            if alias not in prompt.lower() and (time.time() - self.lastCall) > 30:
                return

        self.lastCall = time.time()

        self.logger.user(prompt)

        code = self.handler.handle(prompt)

        self.logger.code(code)

        self.executor.execute(code)
