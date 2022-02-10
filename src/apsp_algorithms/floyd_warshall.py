from typing import Union


def floyd_warshall(adj_matrix: list[list[float]]) -> (list[list[float]], list[list[int]]):
    """ Computes the shortest path between every pair of nodes

    The Floyd Warshall algorithm answer the APSP problem : it computes the shortest distance between every pair
    of nodes and allows constructing the path in O(E) time for every pair.

    Args:
        adj_matrix: A weighted graph represented as an adjacency matrix. Nodes that cannot access each other must
            have an infinite edge weight. Self-edges (edges from i to i) are assumed to be of weight 0.
    Returns:
        A tuple containing a Distance matrix and a Next matrix
        Distance matrix : distance[i][j] is the length of the optimal path from node i to node j
        Next matrix : Allows the reconstruction of the shortest path from i to j by calling the helper function with
            args i, j, Next
    """
    # Steps of the floyd warshall algorithm :
    # Create a dist matrix initialized with the edge value of the adjacency matrix of the graph

    n = len(adj_matrix)
    dist_matrix: list[list[float]] = [[f for f in line] for line in adj_matrix]
    temp_matrix: list[list[float]] = [[0] * n for _ in range(n)]
    next_matrix: list[list[Union[int, None]]] = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != float('inf'):
                next_matrix[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                    temp_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    next_matrix[i][j] = next_matrix[i][k]
                else:
                    temp_matrix[i][j] = dist_matrix[i][j]
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = temp_matrix[i][j]
    return dist_matrix, next_matrix


def path_reconstruction(i: int, j: int, next_matrix: list[list[Union[int, None]]]) -> Union[list[int], None]:
    """ Compute the optimal path from node i to node j

    The path reconstruction function lets us reconstruct the optimal path from i to j using the next matrix
    computed with the floyd-warshall algorithm.

    Args:
        i: The index of the start node
        j: The index of the end node
        next_matrix: The next matrix computed during the floyd-warshall algorithm execution.
    Returns:
        A list of indexes that start with the start node's index and end with the end node's index representing the
        optimal path from the start node the end node.
    """
    # Each column j in the next matrix can be seen as a "prev array" for node j, that is, to go from node i to node j,
    # one should first visit k = next_matrix[i][j], then next[k][j], etc... util we reach j
    if next_matrix[i][j] is None:
        return None

    optimal_path = [i]
    k = next_matrix[i][j]
    while k != j:
        optimal_path.append(k)
        k = next_matrix[k][j]

    optimal_path.append(j)
    return optimal_path
