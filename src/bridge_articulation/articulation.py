from typing import Union


def find_articulation_points(graph: list[list[int]]) -> list[bool]:
    """ Find the articulation points of the given input undirected graph

    This algorithm finds the articulation points of a graph in O(V+E) time. An articulation point is a vertex of the
    graph that, if removed, would increase the number of connected components.

    Args:
        graph: A graph represented as an adjacency list
    Returns:
        A list containing the indices of all the articulation points of the input graph
    """


    visited: list[bool] = [False] * len(graph)
    depths: list[int] = [-1] * len(graph)
    low_link_values: list[Union[int, None]] = [None] * len(graph)
    is_art: list[bool] = [False] * len(graph)
    current_depth: int = 0
    start_node: int = 0
    out_edge_count: int = 0

    def dfs(node: int, parent: int):
        nonlocal current_depth
        nonlocal start_node
        nonlocal out_edge_count
        depths[node] = current_depth
        low_link_values[node] = current_depth
        if parent == start_node:
            out_edge_count += 1
        current_depth += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor, node)
                low_link_values[node] = min(low_link_values[node], low_link_values[neighbor])
                if depths[node] <= low_link_values[neighbor]:
                    is_art[node] = True
            else:
                low_link_values[node] = min(low_link_values[node], depths[neighbor])
        print(f'Node: {node}, ID : {depths[node]}, Low-link : {low_link_values[node]}')

    for start in range(len(graph)):
        if not visited[start]:
            out_edge_count = 0
            start_node = start
            visited[start] = True
            dfs(start, -1)
            is_art[start_node] = out_edge_count > 1

    return is_art
