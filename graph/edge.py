from abc import ABC, abstractmethod


class AbstractEdge(ABC):
    @abstractmethod
    def getStart(self) -> int:
        pass

    @abstractmethod
    def getEnd(self) -> int:
        pass

    @abstractmethod
    def getWeight(self) -> float:
        pass
