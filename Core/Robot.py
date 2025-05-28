from Core.Dispatcher import AbstractDispatcher
from Core.UserInterface import UserInterface
from Logger.Logger import Logger


class Robot:
    def __init__(self, logger: Logger, dispatcher: AbstractDispatcher):
        self.dispatcher = dispatcher
        self.logger = logger

    def run(self, ui: UserInterface):
        self.dispatcher.start(ui)
