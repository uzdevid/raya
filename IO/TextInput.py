from IO.Input import Input


class TextInput(Input):
    def getPrompt(self, message: str = None):
        return input(f"{message}: ")
