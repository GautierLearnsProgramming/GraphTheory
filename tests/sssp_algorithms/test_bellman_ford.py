from src.sssp_algorithms.bellman_ford import bellman_ford
from src.graph_utils.conversion import weighted_adj_map_to_adj_list


def test_bellman_ford():
    adj_map = {
        0: [(1, 1), (2, 1)],
        1: [(3, 3), (4, 2)],
        2: [(3, 1)],
        3: [(4, -5)],
        4: [(1, 1)]
    }

    adj_list, list_to_map = weighted_adj_map_to_adj_list(adj_map)
    assert ([0, float('-inf'), 1, float('-inf'), float('-inf')], [0, 4, 0, 1, 3]) == bellman_ford(adj_list, 0)
