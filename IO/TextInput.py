from IO.Input import Input


class TextInput(Input):
    def getPrompt(self, message: str = None):
        if message is None:
            message = 'Prompt'

        return input(f"{message}: ")
