import keyboard

from Context.CtxModule import CtxModule


class ActiveWindow(CtxModule):
    def getSelectedText(self):
        clipboard = self.ctx.clipboard

        previous = clipboard.getContent()

        keyboard.press_and_release('ctrl + c')
        # time.sleep(0.2)

        selected_text = clipboard.getContent()

        clipboard.copy(previous)

        return selected_text
