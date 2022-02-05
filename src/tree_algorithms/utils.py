def deleteNode(graph: dict[int, list[int]], node_index: int):
    neighbors = graph.pop(node_index)
    for neighbor_index in neighbors:
        graph[neighbor_index].remove(node_index)