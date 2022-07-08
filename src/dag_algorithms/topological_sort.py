# The topSort function assumes that the graph passed to it is a directed acyclic graph.
def topsort(dag: list[list[int]]):
    """ Orders a directed acyclic graph topologically

        Args:
            dag: A directed acyclic graph
        Returns:
            A topological order of the graph
        """
    top_order = []
    visited = [False] * len(dag)

    def dfs(node: int):
        visited[node] = True
        for child in dag[node]:
            if not visited[child]:
                dfs(child)
        top_order.append(node)

    for start_node in range(len(dag)):
        if not visited[start_node]:
            dfs(start_node)

    top_order.reverse()
    return top_order

