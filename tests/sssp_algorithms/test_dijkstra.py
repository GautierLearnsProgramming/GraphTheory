from src.sssp_algorithms.dijkstra import dijkstra_lazy
import src.graph_utils.conversion as conversion
from typing import Callable


def dijkstra_test(dijkstra: Callable[[list[list[tuple[int, float]]], int], tuple[list[float], list[int]]]):
    graph = {
        0: [(1, 1), (2, 2), (4, 1)],
        1: [(0, 1), (3, 5), (6, 1)],
        2: [(0, 2), (3, 3), (7, 4)],
        3: [(2, 3), (1, 5), (5, 6), (8, 5), (10, 15)],
        4: [(0, 1), (7, 4)],
        5: [(3, 6), (8, 2)],
        6: [(1, 1), (9, 9)],
        7: [(2, 4), (4, 4), (8, 1)],
        8: [(7, 1), (3, 5), (5, 2)],
        9: [(10, 1), (6, 9)],
        10: [(9, 1), (3, 15)]
    }

    weighted_adj_list, _ = conversion.weighted_adj_map_to_adj_list(graph)
    assert dijkstra(weighted_adj_list, 0) == ([0, 1, 2, 5, 1, 8, 2, 5, 6, 11, 12], [-1, 0, 0, 2, 0, 8, 1, 4, 7, 6, 9])


def test_dijkstra_lazy():
    dijkstra_test(dijkstra_lazy)
