from typing import Union


def find_articulation_points(graph: list[list[int]]) -> list[int]:
    """ Find the articulation points of the given input graph

    This algorithm finds the articulation points of a graph in O(V+E) time. An articulation point is a vertex of the
    graph that, if removed, would increase the number of connected components.

    Args:
        graph: A graph represented as an adjacency list
    Returns:
        A list containing the indices of all the articulation points of the input graph
    """
    # Build the dfs tree of the graph. On the recursive callback, in post-order traversal, update the low-link value
    # After the traversal of every children, check if the id of the node is lower than or equal to the low-link value of
    # the node. In the case it is, the node is an articulation point.

    articulation_points: list[int] = []
    visited: list[bool] = [False] * len(graph)
    depths: list[int] = [-1] * len(graph)
    low_link_values: list[Union[int, None]] = [None] * len(graph)
    current_depth: int = 0
    start_node: int = 0

    def dfs(node: int, parent: int):
        nonlocal current_depth
        nonlocal start_node
        depths[node] = current_depth
        low_link_values[node] = current_depth
        current_depth += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor, node)
            low_link_values[node] = min(low_link_values[node], low_link_values[neighbor])
        for neighbor in graph[node]:
            if depths[node] <= low_link_values[neighbor] and start_node != node:
                if not articulation_points.__contains__(node):
                    articulation_points.append(node)

    for start in range(len(graph)):
        if not visited[start]:
            start_node = start
            visited[start] = True
            dfs(start, -1)

    return articulation_points
