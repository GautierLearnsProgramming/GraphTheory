from abc import ABC, abstractmethod
from collections.abc import Iterable
from graph.edge import AbstractEdge


class AbstractVertex(ABC):
    @abstractmethod
    def iter_edges(self) -> Iterable[AbstractEdge]:
        pass

    @abstractmethod
    def get_edges(self) -> list[AbstractEdge]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_index(self) -> int:
        pass
