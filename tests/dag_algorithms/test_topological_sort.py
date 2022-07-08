from src.dag_algorithms.topological_sort import topsort
import src.graph_utils.conversion as conversion
from typing import Callable


def top_sort_tester(top_sort: Callable[[list[list[int]]], list[int]]):
    graph = {
        0: [(1, 5), (2, 1)],
        1: [(5, 3), (4, 3), (3, 6)],
        2: [(3, 2)],
        3: [(4, 4)],
        4: [(5, 1), (6, 6)],
        5: [(6, 2)],
        6: [(7, 2)],
        7: []
    }

    unweighted_graph = conversion.weighted_adj_map_to_unweighted_adj_map(graph)
    adj_list, _ = conversion.adj_map_to_adj_list(unweighted_graph)
    sorted_graph = top_sort(adj_list)

    print(sorted_graph)

    assert sorted_graph.index(0) < sorted_graph.index(1)
    assert sorted_graph.index(0) < sorted_graph.index(2)
    assert sorted_graph.index(2) < sorted_graph.index(3)
    assert sorted_graph.index(3) < sorted_graph.index(4)
    assert sorted_graph.index(1) < sorted_graph.index(3)
    assert sorted_graph.index(1) < sorted_graph.index(4)
    assert sorted_graph.index(1) < sorted_graph.index(5)
    assert sorted_graph.index(4) < sorted_graph.index(5)
    assert sorted_graph.index(4) < sorted_graph.index(6)
    assert sorted_graph.index(6) < sorted_graph.index(7)


def test_top_sort():
    top_sort_tester(topsort)
