from Core.Handler import AbstractHandler
from IO.Input import Input
from IO.Output import Output
from Logger.Logger import Logger


class UserInterface:
    def __init__(self, input: Input, output: Output, handler: AbstractHandler, logger: Logger):
        self.input = input
        self.output = output
        self.handler = handler
        self.logger = logger

    def ask(self, question: str):
        self.logger.assistant(question)
        self.output.speak(question)

        answer = self.input.getPrompt(question)
        self.speak(self.handler.subHandle(question, answer))

    def speak(self, text: str):
        self.logger.assistant(text)
        self.output.speak(text)

    def print(self, text: str):
        self.logger.assistant(text)
        print('Raya: ' + text)
