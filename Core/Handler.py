from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def handle(self, query: str) -> str:
        pass
