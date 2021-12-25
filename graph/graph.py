from abc import ABC, abstractmethod
from graph.edge import AbstractEdge
from graph.vertex import AbstractVertex
from collections.abc import Iterable


class Graph(ABC):
    @abstractmethod
    def iter_edges(self) -> Iterable[AbstractEdge]:
        pass

    @abstractmethod
    def iter_vertices(self) -> Iterable[AbstractVertex]:
        pass

    @abstractmethod
    def getVertex(self, index: int) -> AbstractVertex:
        pass

    @abstractmethod
    def vertex(self):
        pass

    @abstractmethod
    def edge(self, start: int, end: int, weight: float):
        pass

    @abstractmethod
    def is_directed(self) -> bool:
        pass

    @abstractmethod
    def is_weighted(self) -> bool:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
