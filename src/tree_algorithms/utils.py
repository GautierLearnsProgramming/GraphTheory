# Delete node at node_index. This function assumes an UNDIRECTED graph. In the case of a directed graph, the node might
# still in some edge lists
def deleteNode(graph: dict[int, list[int]], node_index: int):
    neighbors = graph.pop(node_index)
    for neighbor_index in neighbors:
        graph[neighbor_index].remove(node_index)


def copyUndirectedGraph(graph: dict[int, list[int]]) -> dict[int, list[int]]:
    return {node_index: [neighbor for neighbor in neighbors] for node_index, neighbors in graph.items()}
