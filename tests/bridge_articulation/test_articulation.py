from src.bridge_articulation.articulation import find_articulation_points
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
