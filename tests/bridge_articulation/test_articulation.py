from typing import Callable

from src.bridge_articulation.articulation import find_articulation_points
import src.bridge_articulation.articulation_training as training
from src.graph_utils.conversion import adj_map_to_adj_list


def test_articulation():
    adj_map_1 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    adj_map_2 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1, 4, 5],
        4: [3, 5],
        5: [3, 4]
    }

    adj_map_3 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3, 4],
        3: [2, 4],
        4: [2, 3]
    }

    adj_list_1, list_to_map_1 = adj_map_to_adj_list(adj_map_1)
    assert find_articulation_points(adj_list_1) == [False, False, False, False]

    adj_list_2, list_to_map_2 = adj_map_to_adj_list(adj_map_2)
    assert find_articulation_points(adj_list_2) == [False, True, False, True, False, False]

    adj_list_3, list_to_map_3 = adj_map_to_adj_list(adj_map_3)
    assert find_articulation_points(adj_list_3) == [False, False, True, False, False]


def articulation_tester(tested: Callable[[list[list[int]]], list[int]]):
    adj_map = {
        0: [1, 4],
        1: [0, 4],
        2: [3, 4, 5],
        3: [2, 4],
        4: [0, 1, 2, 3],
        5: [6, 2],
        6: [5]
    }

    adj_list, _ = adj_map_to_adj_list(adj_map)

    articulation_points = tested(adj_list)
    assert articulation_points.__contains__(4)
    assert articulation_points.__contains__(5)
    assert articulation_points.__contains__(2)
    assert not articulation_points.__contains__(0)


def test_articulation_training():
    articulation_tester(training.find_articulation_points)
