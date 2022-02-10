from typing import Union


def bellman_ford(graph: list[list[tuple[int, float]]], source_index: int) -> tuple[list[float], list[Union[int, None]]]:
    """ Compute the shortest path to every node from the given source node, including negative cycles

    The Bellman-Ford algorithm is a SSSP algorithm that runs in O(V+E) time and computes the shortest path to every
    node from a given source node. This version also detects and propagates negative cycles.

    Args:
        graph: A graph represented as an adjacency list
        source_index: The index of the source node in the adjacency list
    Returns:
        A tuple containing :
        - The list of the distances to every node form the start node
        - A prev array that can be used to compute the shortest path from the starting node to every node in O(E) time
    """
    # The Bellman-Ford algorithm iterates through the list of edges V-1 where V is the number of vertices.
    # We maintain in memory a dist array that contains the currently known shortest path to every node and a prev array
    # that contains, for each node, its previous node in the shortest path relative to the source node
    # Each time we iterate over an edge, we try to relax it.

    dist: list[float] = [float('inf')] * len(graph)
    prev: list[Union[int, None]] = [None] * len(graph)

    dist[source_index] = 0
    prev[source_index] = source_index

    for k in range(len(graph) - 1):
        for node_index, edge_list in enumerate(graph):
            for edge in edge_list:
                if dist[node_index] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[node_index] + edge[1]
                    prev[edge[0]] = node_index

    # At this point of the algorithm, the dist array contains the best path in the absence of negative cycles. The next
    # part of the algorithms allows detection and propagation of negative cycles.

    for k in range(len(graph) - 1):
        for node_index, edge_list in enumerate(graph):
            for edge in edge_list:
                if dist[node_index] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = float('-inf')
                    prev[edge[0]] = node_index

    return dist, prev
