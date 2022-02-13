from src.bridge_articulation.bridge import find_bridges
from src.graph_utils.conversion import adj_map_to_adj_list


def test_find_bridges():
    adj_map = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 3, 7],
        3: [2, 4, 6],
        4: [3, 5],
        5: [4, 6],
        6: [3, 5],
        7: [2, 8],
        8: [7]
    }
    adj_list, list_to_map = adj_map_to_adj_list(adj_map)
    bridges = find_bridges(adj_list)
    assert bridges.__contains__((2, 3)) or bridges.__contains__((3, 2))
    assert bridges.__contains__((7, 8)) or bridges.__contains__((8, 7))
    assert bridges.__contains__((2, 7)) or bridges.__contains__((7, 2))
