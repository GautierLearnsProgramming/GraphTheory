from src.tree_algorithms import graph


tree = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }

graph.deleteNode(tree, 1)
print(tree)
