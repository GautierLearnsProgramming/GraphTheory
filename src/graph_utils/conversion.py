WeightedEdge = tuple[int, float]

def adj_map_to_adj_list(adj_map: dict[int, list[int]]) -> tuple[list[list[int]], dict[int, int]]:
    adj_list = []
    list_to_map = {}
    map_to_list = {}
    for index, node_index in enumerate(adj_map):
        map_to_list[node_index] = index
        list_to_map[index] = node_index
    for node_index, neighbors in adj_map.items():
        adj_list.append([map_to_list[neighbor] for neighbor in neighbors])
    return adj_list, list_to_map


def adj_list_to_adj_map(adj_list: list[list[int]], list_to_map: dict[int, int]):
    adj_map = {}
    for index, neighbors in enumerate(adj_list):
        adj_map[list_to_map[index]] = [list_to_map[neighbor] for neighbor in neighbors]
    return adj_map


def weighted_adj_map_to_adj_list(
        adj_map: dict[int, list[WeightedEdge]]) -> tuple[list[list[WeightedEdge]], dict[int, int]]:
    adj_list: list[list[WeightedEdge]] = []
    list_to_map = {}
    map_to_list = {}
    for index, node_index in enumerate(adj_map):
        map_to_list[node_index] = index
        list_to_map[index] = node_index
    for node_index, edges in adj_map.items():
        adj_list.append([(map_to_list[edge[0]], edge[1]) for edge in edges])
    return adj_list, list_to_map


def weighted_adj_list_to_adj_map(
        adj_list: list[list[WeightedEdge]], list_to_map: dict[int, int]) -> dict[int, list[WeightedEdge]]:
    adj_map: dict[int, list[WeightedEdge]] = {}
    for index, edges in enumerate(adj_list):
        adj_map[list_to_map[index]] = [(list_to_map[edge[0]], edge[1]) for edge in edges]
    return adj_map


def weighted_adj_list_to_adj_matrix(adj_list: list[list[WeightedEdge]]) -> list[list[float]]:
    adj_matrix = [[float('inf') for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    for index, edges in enumerate(adj_list):
        for edge in edges:
            adj_matrix[index][edge[0]] = edge[1]
    return adj_matrix


def weighted_adj_matrix_to_adj_list(adj_matrix: list[list[float]]) -> list[list[WeightedEdge]]:
    adj_list: list[list[WeightedEdge]] = []
    for node_index, edges_weights in enumerate(adj_matrix):
        adj_list.append([])
        for neighbor_index, edge_weight in enumerate(edges_weights):
            if edge_weight != float('inf'):
                adj_list[node_index].append((neighbor_index, edge_weight))
    return adj_list


def weighted_adj_map_to_unweighted_adj_map(adj_map: dict[int, list[WeightedEdge]]) -> dict[int, list[int]]:
    unweighted_adj_map = {}
    for node in adj_map:
        unweighted_adj_map[node] = [child for (child, _) in adj_map[node]]
    return unweighted_adj_map
