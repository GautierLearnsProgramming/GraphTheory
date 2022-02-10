from __future__ import annotations
from typing import Union
import heapq


def dijkstra_lazy(graph: list[list[tuple[int, float]]], start_node: int) -> tuple[list[float], list[int]]:
    """ Compute the shortest path to every node in the graph from a given starting node

    Args:
        graph: A graph represented as an adjacency list, with only non-negative edge weights
        start_node: The index of the starting node
    Returns:
        A tuple containing :
        - The distance from the starting node to every node in the graph
        - A prev array allowing reconstruction of the path from the start node to any other node
    """

    # The DistPair class is used to store (index, distance_from_start) pairs in a priority queue
    class DistPair:
        def __init__(self, node_index: int, dist: float):
            self.node_index = node_index
            self.dist = dist

        def __lt__(self, other: DistPair):
            return self.dist <= other.dist

        def __gt__(self, other):
            return self.dist > other.dist

    # Dijkstra algorithm works by maintaining a priority queue of the most promising key-value pairs
    # At each step, we pop the most promising key-value pair from the heapq, and relax each of its edges
    # The algorithm is finished once the heapq is empty

    visited = [False] * len(graph)
    prev: list[Union[int, None]] = [None] * len(graph)
    dist: list[float] = [float('inf')] * len(graph)
    pq: list[DistPair] = []

    # Initialize the variables with the starting node
    dist[start_node] = 0
    prev[start_node] = start_node
    heapq.heappush(pq, DistPair(start_node, 0))

    # While the priority queue is not empty, pop the most promising index-dist pair
    # If the node has already been visited, it means the key-distance pair was not relevant anymore and we continue
    # Otherwise, we relax each outgoing edge from the node, and in the case we get an improvement, we add the
    # improved key-distance pair to the priority queue
    while pq:
        current = heapq.heappop(pq)
        if visited[current.node_index]:
            continue
        visited[current.node_index] = True
        for neighbor in graph[current.node_index]:
            if not visited[neighbor[0]]:
                # Edge relaxation
                if dist[current.node_index] + neighbor[1] < dist[neighbor[0]]:
                    dist[neighbor[0]] = dist[current.node_index] + neighbor[1]
                    prev[neighbor[0]] = current.node_index
                    heapq.heappush(pq, DistPair(neighbor[0], dist[neighbor[0]]))

    return dist, prev

