import pyperclip

from Context.CtxModule import CtxModule


class Clipboard(CtxModule):
    def getContent(self):
        return pyperclip.paste()

    def copy(self, text: str):
        return pyperclip.copy(text)
