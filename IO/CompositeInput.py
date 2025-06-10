import threading

from IO.Input import Input


class CompositeInput(Input):
    def __init__(self, inputMethods: list):
        self.inputMethods = inputMethods

        self.result = None
        self.isLock = threading.Lock()

    def __getPrompt(self, method: Input, message: str = None):
        result = method.getPrompt(message)

        with self.isLock:
            if self.result is None and result:
                self.result = result

    def getPrompt(self, message: str = None):
        for method in self.inputMethods:
            thread = threading.Thread(target=self.__getPrompt, args=(method, message))
            thread.start()

        while True:
            with self.isLock:
                if self.result is not None:
                    result = self.result
                    self.result = None
                    return result
