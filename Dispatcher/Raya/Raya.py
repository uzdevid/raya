from Core.Dispatcher import AbstractDispatcher
from Core.Executor import AbstractExecutor
from Dispatcher.Raya.Handler import Handler
from Logger.Logger import Logger


class Dispatcher(AbstractDispatcher):
    aliases = ['рая']

    def __init__(self, handler: Handler, executor: AbstractExecutor, logger: Logger):
        self.handler = handler
        self.executor = executor
        self.logger = logger

    def getAliases(self) -> list:
        return ['рая']

    def start(self, prompt: str):
        self.logger.user(prompt)

        code = self.handler.handle(prompt)

        self.logger.code(code)

        self.executor.execute(code)
