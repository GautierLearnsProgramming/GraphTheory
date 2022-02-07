import src.apsp_algorithms.floyd_warshall as fw


def test_floyd_warshall():
    adj_matrix = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]

    dist_matrix = [[0, 1, 3], [1, 0, 2], [3, 2, 0]]
    next_matrix = [[0, 1, 1], [0, 1, 2], [1, 1, 2]]

    assert dist_matrix, next_matrix == fw.floyd_warshall(adj_matrix)
