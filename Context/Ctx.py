import os

from Context.ActiveWindow import ActiveWindow
from Context.AppManager import AppManager
from Context.Clipboard import Clipboard
from Context.FileSystem import FileSystem
from Core.UserInterface import UserInterface
from Memory.Memory import Memory


class Ctx:
    def __init__(self, ui: UserInterface, memory: Memory):
        self.ui = ui
        self.os = os
        self.memory = memory
        self.clipboard = Clipboard().withCtx(self)
        self.fileSystem = FileSystem().withCtx(self)
        self.activeWindow = ActiveWindow().withCtx(self)
        self.appManager = AppManager().withCtx(self)
