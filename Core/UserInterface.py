from IO.Input import Input
from IO.Output import Output
from Logger.Logger import Logger

class UserInterface:
    def __init__(self, input: Input, output: Output, logger: Logger):
        self.input = input
        self.output = output
        self.logger = logger

    def ask(self, question: str):
        self.logger.assistant(question)
        self.output.speak(question)

        return self.input.get(question)

    def speak(self, text: str):
        self.logger.assistant(text)
        self.output.speak(text)

    def print(self, text: str):
        self.logger.assistant(text)
        print('Raya: ' + text)
