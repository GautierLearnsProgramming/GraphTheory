from graph.edge import AbstractEdge


class Edge(AbstractEdge):
    def getStart(self) -> int:
        return self.u

    def getEnd(self) -> int:
        return self.v

    def getWeight(self) -> float:
        return self.w

    def __init__(self, u: int, v: int, w: float):
        self.u = u
        self.v = v
        self.w = w

    def __eq__(self, other):
        if self.u != other.u:
            return False
        if self.v != other.v:
            return False
        if self.w != other.w:
            return False
        return True

    def __hash__(self):
        return self.u * 32452867 + self.v * 32452867 ** 2
