from abc import ABC


class CtxModule(ABC):
    ctx: None

    def withCtx(self, ctx):
        self.ctx = ctx
        return self
