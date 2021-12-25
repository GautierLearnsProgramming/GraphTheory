from typing import Iterable

from adj_list_rep.edge import Edge
from graph.edge import AbstractEdge
from graph.vertex import AbstractVertex


class Vertex(AbstractVertex):
    def get_index(self) -> int:
        return self.index

    def get_name(self) -> str:
        if self.name == "":
            return str(self.index)
        return self.name

    def iter_edges(self) -> Iterable[AbstractEdge]:
        for e in self.edges:
            yield e

    def get_edges(self) -> list[AbstractEdge]:
        return self.edges

    # What should a vertex contain ?
    # A vertex should contains its value, optionally a name, a list of edges,
    def __init__(self, index: int, value=None, name=""):
        self.index = index
        self.value = value
        self.name = name
        self.edges: list[Edge] = []

    def edge(self, u: int, v: int, w: float = 1):
        self.edges.append(Edge(u, v, w))

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
