from graph.graph import Graph
from graph.edge import AbstractEdge
from graph.vertex import AbstractVertex
from collections import deque


# Algorithm description:
# initialize a stack with the node we're starting from
# as long as the stack is not empty, pop the node on top of the stack (so the last added), set it to visited
# operate on the node, append the stack with each non-visited node
def dfs(graph: Graph, start_index: int = 0):
    if graph.get_size() <= start_index:
        return
    visited = [False for _ in range(graph.get_size())]
    stack: deque[AbstractVertex] = deque()
    stack.append(graph.getVertex(start_index))
    visited[start_index] = True
    while stack:
        vertex = stack.pop()
        print(f'{vertex.get_name()} ')
        for e in vertex.iter_edges():
            if not visited[e.getEnd()]:
                stack.append(graph.getVertex(e.getEnd()))
                visited[e.getEnd()] = True


def bfs(graph: Graph, start_index: int = 0):
    if graph.get_size() <= start_index:
        return
    visited = [False for _ in range(graph.get_size())]
    queue: deque[AbstractVertex] = deque()
    queue.append(graph.getVertex(start_index))
    visited[start_index] = True
    while queue:
        vertex = queue.popleft()
        print(vertex.get_name())
        for e in vertex.iter_edges():
            if not visited[e.getEnd()]:
                visited[e.getEnd()] = True
                queue.append(graph.getVertex(e.getEnd()))
