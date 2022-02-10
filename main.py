from src.apsp_algorithms.floyd_warshall import floyd_warshall, path_reconstruction

tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
        }

dag = [
        [1],
        [2, 3],
        [3],
        []
        ]

weighted_graph = {
        1: [(2, 3), (3, 5)],
        2: [(1, 1)],
        3: [],
        4: [(3, -1)]
}

adj_matrix = [
        [0, 1, 4, float('inf')],
        [1, 0, 2, float('inf')],
        [4, 2, 0, float('inf')],
        [3, float('inf'), float('inf'), 0]
]
dist_matrix, next_matrix = floyd_warshall(adj_matrix)
print(f'dist matrix: {dist_matrix}')
print(f'next matrix: {next_matrix}')
print(f'optimal path: {path_reconstruction(1, 3, next_matrix)}')
