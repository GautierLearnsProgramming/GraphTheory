from typing import Callable
from src.graph_utils.conversion import adj_map_to_adj_list


def tarjan_tester(tarjan_function: Callable[[list[list[int]]], list[set[int]]]):
    adj_map = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4, 5],
        4: [8, 3],
        5: [6],
        6: [7],
        7: [5],
        8: []
    }
    adj_list, _ = adj_map_to_adj_list(adj_map)
    sccs = tarjan_function(adj_list)
    assert sccs.__contains__({0, 1, 2})
    assert sccs.__contains__({3, 4})
    assert sccs.__contains__({8})
    assert sccs.__contains__({5, 6, 7})
