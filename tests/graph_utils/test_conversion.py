import src.graph_utils.conversion as conversion


def test_unweighted_conversions():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
    }

    adj_list = [[1], [0, 2], [1, 3, 4], [2], [2]]
    list_to_map = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    assert adj_list, list_to_map == conversion.adj_map_to_adj_list(graph)
    assert graph == conversion.adj_list_to_adj_map(adj_list, list_to_map)


def test_weighted_map_list_conversions():
    weighted_graph = {
        1: [(2, 3), (3, 5)],
        2: [(1, 1)],
        3: [],
        4: [(3, -1)]
    }

    weighted_adj_list = [[(1, 3), (2, 5)], [(0, 1)], [], [(2, -1)]]
    list_to_map = {0: 1, 1: 2, 2: 3, 3: 4}

    assert weighted_adj_list, list_to_map == conversion.weighted_adj_map_to_adj_list(weighted_graph)
    assert weighted_graph == conversion.weighted_adj_list_to_adj_map(weighted_adj_list, list_to_map)


def test_weighted_list_matrix_conversions():
    weighted_adj_list = [[(1, 3), (2, 5)], [(0, 1)], [], [(2, -1)]]
    adj_matrix = [[float('inf'), 3, 5, float('inf')],
                  [1, float('inf'), float('inf'), float('inf')],
                  [float('inf'), float('inf'), float('inf'),
                   float('inf')], [float('inf'), float('inf'), -1, float('inf')]]

    assert conversion.weighted_adj_matrix_to_adj_list(adj_matrix) == weighted_adj_list
    assert conversion.weighted_adj_list_to_adj_matrix(weighted_adj_list) == adj_matrix
