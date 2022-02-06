# The topSort function assumes that the graph passed to it is a directed acyclic graph.
def topSort(graph: list[list[int]]) -> list[int]:
    """ Orders a directed acyclic graph topologically

    Args:
        graph: A directed acyclic graph
    Returns:
        A topological order of the graph
    """
    # The topsort algorithm works by depth-first searching through the graph and adding encountered nodes to the
    # topological ordering in reverse order.

    visited = [False for _ in graph]
    topologicalOrder: list[int] = []

    # DFS from node 0, then go through the visited array and find the next unvisited node. Repeat the DFS from there
    # keep going until all nodes have been visited
    dfs_start_index = 0
    visited[dfs_start_index] = True
    while dfs_start_index < len(graph):
        topSortRecursiveCallback(dfs_start_index, graph, visited, topologicalOrder)
        while dfs_start_index < len(graph) and visited[dfs_start_index]:
            dfs_start_index += 1
    topologicalOrder.reverse()
    return topologicalOrder


def topSortRecursiveCallback(node_index: int, graph: list[list[int]], visited: list[bool], partialTopologicalOrder: list[int]):
    for child_index in graph[node_index]:
        if not visited[child_index]:
            visited[child_index] = True
            topSortRecursiveCallback(child_index, graph, visited, partialTopologicalOrder)
    partialTopologicalOrder.append(node_index)
