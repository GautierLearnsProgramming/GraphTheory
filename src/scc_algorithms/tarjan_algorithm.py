from typing import Union


def tarjan_scc_algorithm(graph: list[list[int]]):
    """ Decompose the input directed graph into a partition of strongly connected components

    Tarjan's algorithm decomposes the graph into a partition of strongly connected components in O(V+E) time, where a
    strongly connected component is defined as a subgraph where each node of a given subgraph is connected to every
    other node of the subgraph.

    Args:
        graph: An undirected graph represented as an adjacency list
    Returns:
        A partition of the graph into SCCs represented as a list of list, where each sublist represents a strongly
        connected component.
    """

    stack: list[int] = []
    on_stack: list[bool] = [False] * len(graph)
    visited: list[bool] = [False] * len(graph)
    indexes: list[int] = [-1] * len(graph)
    low_links: list[int] = [-1] * len(graph)

    current_index: int = 0

    strongly_connected_components = []

    def dfs(node):
        # Initialize the index and low-link value of the node
        nonlocal current_index
        indexes[node] = current_index
        low_links[node] = current_index
        current_index += 1

        visited[node] = True

        stack.append(node)
        on_stack[node] = True

        # For every neighbor of the node, dfs through them if they are not visited, and update the low-link value
        # There are two cases: in the node was unvisited, take the minimum of the low-links, otherwise, if and only if
        # the node is on the stack, take the minimum of the low-link and the neighbor's index
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                low_links[node] = min(low_links[node], low_links[neighbor])
            else:
                if on_stack[neighbor]:
                    low_links[node] = min(low_links[node], indexes[neighbor])

        # At this point, if the low-link of the node is equal to its index, it means that the node starts an SCC and we
        # can pop the stack until we reach it to get that SCC.
        if low_links[node] == indexes[node]:
            scc = []
            while True:
                scc_member = stack.pop()
                on_stack[scc_member] = False
                scc.append(scc_member)
                if scc_member == node:
                    break
            strongly_connected_components.append(scc)

    return strongly_connected_components
