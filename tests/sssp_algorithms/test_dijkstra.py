from src.sssp_algorithms.dijkstra import dijkstra_lazy
from src.graph_utils.conversion import weighted_adj_map_to_adj_list


def test_dijkstra_lazy():
    adj_map = {
        0: [(1, 1), (2, 1)],
        1: [(3, 3), (4, 2)],
        2: [(3, 1)],
        3: [],
        4: []
    }

    adj_list, _ = weighted_adj_map_to_adj_list(adj_map)

    assert ([0, 1, 1, 2, 3], [0, 0, 0, 2, 1]) == dijkstra_lazy(adj_list, 0)
    assert ([float('inf'), 0, float('inf'), 3, 2], [None, 1, None, 1, 1]) == dijkstra_lazy(adj_list, 1)
