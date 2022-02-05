import src.tree_algorithms.utils
from src.tree_algorithms import center


tree = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }

src.tree_algorithms.utils.deleteNode(tree, 1)
print(tree)
