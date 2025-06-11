import time

from Core.Dispatcher import AbstractDispatcher
from Core.UserInterface import UserInterface
from Logger.Logger import Logger


class Robot:
    lastCall: float = time.time()

    def __init__(self, logger: Logger, dispatcher: AbstractDispatcher):
        self.dispatcher = dispatcher
        self.logger = logger

    def run(self, ui: UserInterface):
        prompt = ui.input.getPrompt()

        for alias in self.dispatcher.getAliases():
            if alias not in prompt.lower() and (time.time() - self.lastCall) > 30:
                return

        self.lastCall = time.time()

        self.dispatcher.start(prompt)
