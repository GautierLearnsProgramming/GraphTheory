def tarjan_algorithm(graph: list[list[int]]) -> list[set[int]]:
    visited = [False] * len(graph)
    indexes = [-1] * len(graph)
    low_link = [-1] * len(graph)
    stack = []
    on_stack = [False] * len(graph)
    sccs: list[set[int]] = []
    current_index = 0

    def tarjan_dfs(node):
        visited[node] = True

        nonlocal current_index
        indexes[node] = current_index
        low_link[node] = current_index
        current_index += 1

        stack.append(node)
        on_stack[node] = True

        for child in graph[node]:
            if not visited[child]:
                tarjan_dfs(child)
                low_link[node] = min(low_link[node], low_link[child])
            else:
                if on_stack[child]:
                    low_link[node] = min(low_link[node], indexes[child])

        if low_link[node] == indexes[node]:
            scc_complete = False
            scc = set()
            while not scc_complete:
                popped = stack.pop()
                on_stack[popped] = False
                scc.add(popped)
                if popped == node:
                    scc_complete = True
            sccs.append(scc)

    for starter in range(len(graph)):
        if not visited[starter]:
            tarjan_dfs(starter)

    return sccs
