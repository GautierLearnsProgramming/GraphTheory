# Delete a node in an undirected graph
from src.tree_algorithms.utils import deleteNode


# Find center returns a list containing one or two integers representing the indexes of the center of the two centers
# The tree is assumed to be UNDIRECTED, which means that any edge (u,v) has a corresponding edge (v,u)
def findCenter(tree: dict[int, list[int]]) -> list[int]:
    # The way to find the centers of a tree is to compute the degree of every node, prune the leaf nodes (nodes with
    # degree 1), and repeat until only one or two nodes are left in the tree
    while len(tree.keys()) > 2:
        leaves = [node_index for node_index, child in tree.items() if len(child) == 1]
        for leaf_index in leaves:
            deleteNode(tree, leaf_index)
    return [node_index for node_index in tree.keys()]
