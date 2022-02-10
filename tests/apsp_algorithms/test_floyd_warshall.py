import src.apsp_algorithms.floyd_warshall as fw


def test_floyd_warshall():
    adj_matrix = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]

    adj_matrix_2 = [
        [0, 1, 4, float('inf')],
        [1, 0, 2, float('inf')],
        [4, 2, 0, float('inf')],
        [3, float('inf'), float('inf'), 0]
    ]

    dist_matrix_2 = [[0, 1, 3, float('inf')], [1, 0, 2, float('inf')], [3, 2, 0, float('inf')], [3, 4, 6, 0]]
    next_matrix_2 = [[0, 1, 1, None], [0, 1, 2, None], [1, 1, 2, None], [0, 0, 0, 3]]

    dist_matrix = [[0, 1, 3], [1, 0, 2], [3, 2, 0]]
    next_matrix = [[0, 1, 1], [0, 1, 2], [1, 1, 2]]

    assert dist_matrix, next_matrix == fw.floyd_warshall(adj_matrix)
    assert dist_matrix_2, next_matrix_2 == fw.floyd_warshall(adj_matrix_2)


def test_path_reconstruction():
    next_matrix = [[0, 1, 1], [0, 1, 2], [1, 1, 2]]
    next_matrix_2 = [[0, 1, 1, None], [0, 1, 2, None], [1, 1, 2, None], [0, 0, 0, 3]]
    assert fw.path_reconstruction(0, 2, next_matrix) == [0, 1, 2]
    assert fw.path_reconstruction(2, 0, next_matrix) == [2, 1, 0]
    assert fw.path_reconstruction(1, 2, next_matrix) == [1, 2]
    assert fw.path_reconstruction(0, 1, next_matrix) == [0, 1]
    assert fw.path_reconstruction(3, 2, next_matrix_2) == [3, 0, 1, 2]
    assert fw.path_reconstruction(1, 3, next_matrix_2) is None
