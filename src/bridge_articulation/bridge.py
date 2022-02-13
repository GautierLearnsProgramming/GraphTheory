from typing import Union


def find_bridges(graph: list[list[int]]) -> [list[tuple[int, int]]]:
    """ Find the bridges of the given input graph

    Find the bridges of the given input graph in O(V+E) time, where a bridge is defined as an edge that, if removed,
    increases the number of connected components in the graph

    Args:
        graph: An unweighted graph represented as an adjacency list
    Returns:
        A list of edges represented as tuple of integers
    """
    # The way the algorithm works in by computing the DFS tree of the graph, where each node is associated an increasing
    # depth number, and computing the low-link value of every node on the recursive callback.

    ids: list[Union[None, int]] = [None] * len(graph)
    low_link: list[Union[None, int]] = [None] * len(graph)
    visited: list[bool] = [False] * len(graph)
    edge_list: list[tuple[int, int]] = []
    current_id = 0

    def dfs(node_index: int, parent_index: int):
        nonlocal current_id
        ids[node_index] = current_id
        low_link[node_index] = current_id
        current_id += 1

        visited[node_index] = True
        for neighbor in graph[node_index]:
            if not visited[neighbor]:
                dfs(neighbor, node_index)
            if neighbor != parent_index:
                low_link[node_index] = min(low_link[node_index], low_link[neighbor])
            if ids[node_index] < low_link[neighbor]:
                edge_list.append((node_index, neighbor))

    for start in range(len(graph)):
        if visited[start]:
            continue
        dfs(start, -1)

    return edge_list
