from src.visualization.visualize import visualize
from src.tree_algorithms.root import rootTree

tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
        }

visualize("newviz", tree)
rooted_tree1 = rootTree(tree, 1)
rooted_tree2 = rootTree(tree, 2)
rooted_tree3 = rootTree(tree, 3)

visualize("rooted_tree1", rooted_tree1, True)
visualize("rooted_tree2", rooted_tree2, True)
visualize("rooted_tree3", rooted_tree3, True)
