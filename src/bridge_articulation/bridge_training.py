def find_bridges(graph: list[list[int]]) -> list[tuple[int, int]]:
    index_list: list[int] = [-1] * len(graph)
    low_link: list[int] = [-1] * len(graph)
    visited: list[bool] = [False] * len(graph)

    bridges: list[tuple[int, int]] = []

    current_index: int = 0

    def bridge_dfs(node: int, parent: int):
        nonlocal current_index

        # Update index, minimum low-link
        index_list[node] = current_index
        low_link[node] = current_index
        current_index += 1

        # Update visited
        visited[node] = True

        for child in graph[node]:
            if child == parent:
                continue
            if not visited[child]:
                bridge_dfs(child, node)
            low_link[node] = min(low_link[node], low_link[child])
            if low_link[child] > index_list[node]:
                bridges.append((node, child))

    for start_node in range(len(graph)):
        if not visited[start_node]:
            bridge_dfs(start_node, -1)


    print(f'index_list: {index_list}')
    print(f'low_link: {low_link}')

    return bridges


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4, 8],
    4: [3, 5, 6, 7],
    5: [4, 6],
    6: [4, 5, 7],
    7: [4, 6],
    8: [3, 9],
    9: [8, 10, 12],
    10: [9, 11],
    11: [10, 12],
    12: [9, 11]
}

from src.graph_utils.conversion import adj_map_to_adj_list
graph_list, graph_dict = adj_map_to_adj_list(graph)

print(find_bridges(graph_list))
