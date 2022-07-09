import heapq as pq


def dijkstra_lazy(graph: list[list[tuple[int, float]]], start_node: int) -> tuple[list[float], list[int]]:
    """ Compute the shortest path to every node in the graph from a given starting node

    Args:
        graph: A weighted graph represented as an adjacency list, with only non-negative edge weights
        start_node: The index of the starting node
    Returns:
        A tuple containing :
        - The distance from the starting node to every node in the graph
        - A prev array allowing reconstruction of the path from the start node to any other node
    """

    n = len(graph)
    prev = [-1] * n
    dist = [float('inf')] * n
    visited = [False] * n
    heap = []

    pq.heappush(heap, (0, start_node))
    dist[start_node] = 0

    while heap:
        node_dist, node = pq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        for child, edge_weight in graph[node]:
            if not visited[child]:
                new_child_dist = node_dist + edge_weight
                if dist[child] > new_child_dist:
                    prev[child] = node
                    dist[child] = new_child_dist
                    pq.heappush(heap, (new_child_dist, child))

    return dist, prev


