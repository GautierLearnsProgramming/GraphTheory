from adj_list_rep.vertex import Vertex
from adj_list_rep.edge import Edge
from graph.graph import Graph
from typing import Iterator
import graphviz

from graph.vertex import AbstractVertex


class AdjacencyList(Graph):
    def getVertex(self, index: int) -> AbstractVertex:
        return self.vertices[index]

    def is_directed(self) -> bool:
        return self.directed

    def is_weighted(self) -> bool:
        return self.weighted

    def get_size(self) -> int:
        return self.size()

    def __init__(self, directed: bool = True, weighted: bool = True):
        self.vertices: list[Vertex] = []
        self.directed = directed
        self.weighted = weighted
        self.name_counter = 0

    def iter_edges(self) -> Iterator[Edge]:
        if self.directed:
            for v in self.vertices:
                for e in v.edges:
                    yield e
        else:
            for v in self.vertices:
                for e in v.edges:
                    if e.u <= e.v:
                        yield e

    def iter_vertices(self) -> Iterator[Vertex]:
        for v in self.vertices:
            yield v

    def size(self):
        return len(self.vertices)

    def edge(self, u: int, v: int, w: float = 1):
        if u >= self.size() or v >= self.size():
            print("Vertex index greater than current number of vertices")
            return
        self.vertices[u].edge(u, v, w)
        if not self.directed:
            self.vertices[v].edge(v, u, w)

    def add_edge(self, edge: Edge):
        if edge.u >= self.size() or edge.v >= self.size():
            print("Edge is incompatible with the current number of vertices")
            return
        else:
            self.vertices[edge.u].edges.append(edge)
            self.vertices[edge.getEnd()].edge(edge.getEnd(), edge.getStart(), edge.getWeight())

    def vertex(self, name: str = "", value=None):
        if name == "":
            if self.name_counter <= 25:
                name = chr(self.name_counter + 65)
            else:
                name = chr(self.name_counter // 26 + 64) + chr(self.name_counter % 26 + 65)
            self.name_counter += 1
        self.vertices.append(Vertex(len(self.vertices), value, name))

    def delete_vertex(self, index: int):
        if index >= self.size():
            return
        self.vertices.pop(index)
        for v in self.iter_vertices():
            if v.get_index() >= index:
                v.index -= 1
        for e in self.iter_edges():
            if e.u >= index:
                e.u -= 1
            if e.v >= index:
                e.v -= 1

    def visualize(self, output_file: str):
        dot = graphviz.Digraph()
        if not self.directed:
            dot = graphviz.Graph()
        for i in range(self.size()):
            v = self.vertices[i]
            if not v.name == "Vertex":
                dot.node(str(i), v.name)
            else:
                dot.node(str(i))
        for e in self.iter_edges():
            if self.weighted:
                dot.edge(str(e.u), str(e.v), str(e.w))
            else:
                dot.edge(str(e.u), str(e.v))

        dot.render(f'doctest-output/{output_file}.gv').replace('\\', '/')
