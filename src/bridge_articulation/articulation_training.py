def find_articulation_points(graph: list[list[int]]):
    n = len(graph)
    visited = [False] * n
    dfs_indexes = [-1] * n
    low_link = [-1] * n
    articulation_points = set()
    dfs_index = 0
    start_edge_count = 0

    def dfs(node: int, parent: int, root: int):
        nonlocal dfs_index
        nonlocal start_edge_count

        visited[node] = True
        dfs_indexes[node] = dfs_index
        low_link[node] = dfs_index
        dfs_index += 1
        if parent == root:
            start_edge_count += 1

        for child in graph[node]:
            if not visited[child]:
                dfs(child, node, root)
                low_link[node] = min(low_link[child], low_link[node])
                if low_link[child] >= dfs_indexes[node]:
                    articulation_points.add(node)
            else:
                low_link[node] = min(low_link[node], dfs_indexes[child])

    for start in range(n):
        if not visited[start]:
            start_edge_count = 0
            dfs(start, -1, start)
            if start_edge_count > 1:
                articulation_points.add(start)
            else:
                if articulation_points.__contains__(start):
                    articulation_points.remove(start)

    return list(articulation_points)
