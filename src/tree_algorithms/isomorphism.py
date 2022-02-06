from src.tree_algorithms.center import findCenter
from src.tree_algorithms.root import rootTree
from src.tree_algorithms.utils import copyUndirectedGraph
from typing import Union
from collections import deque


# This function implements the AHU Tree isomorphism algorithm
# Steps :  - Finding the centers of the trees and root them
# From the leaf
class Node:
    def __init__(self, parent: Union[int, None], children: list[int]):
        self.parent = parent
        self.children = children

    def __str__(self):
        return f'parent: {self.parent}, children: {self.children}'


def rootedTreeToTreeWithParent(tree: dict[int, list[int]]) -> dict[int, Node]:
    graph = {node_index: Node(None, children) for node_index, children in tree.items()}
    for node_index, node in graph.items():
        for child in node.children:
            graph[child].parent = node_index
    return graph


# Parse an undirected tree to its string AHU representation
# Steps :
# - Compute the number of children of every node after rooting from the center
# - Associate a Knuth tuple () to every node without any children
# - For every node whose children all have a string representation, wrap them in () to form the node's rep
# - Repeat the previous step until every node has a string representation
def getAhuRepresentation(tree: dict[int, list[int]], center: int) -> str:
    # The rooted tree in the node form in order to be able to access the parent of a given node
    rootedTree: dict[int, Node] = rootedTreeToTreeWithParent(rootTree(tree, center))
    # The dictionary of number of active children for every node
    activeChildrenDict: dict[int, int] = {}
    # The dictionary of node string representations
    subtreeRepDict: dict[int, str] = {}
    # The queue of nodes to visit next
    nodeQueue: deque[int] = deque()

    # Compute the number of children of each node and queue 0-children nodes
    for node_index, node in rootedTree.items():
        childrenNumber = len(node.children)
        activeChildrenDict[node_index] = childrenNumber
        if childrenNumber == 0:
            nodeQueue.append(node_index)

    while nodeQueue:
        # When a node is popped from the queue, it has no children
        # We can therefore associate a string representation, and decrement its parent active children count
        # If the parent's active children count is 0, we can append it to queue
        rep: str
        current_index = nodeQueue.popleft()
        current = rootedTree[current_index]

        #
        if len(current.children) == 0:
            rep = '()'
        else:
            childrenRep = [subtreeRepDict[child] for child in current.children]
            childrenRep.sort()
            rep = f'({"".join(childrenRep)})'
        subtreeRepDict[current_index] = rep
        if current.parent is not None:
            activeChildrenDict[current.parent] = activeChildrenDict[current.parent] - 1
            if activeChildrenDict[current.parent] == 0:
                nodeQueue.append(current.parent)

    # When the queue is empty, it means every node in the tree has a string representation
    # We can therefore return the center's string rep
    return subtreeRepDict[center]


def areIsomorphic(tree_1: dict[int, list[int]], tree_2: dict[int, list[int]]):
    tree_1_center = findCenter(copyUndirectedGraph(tree_1))
    tree_2_center = findCenter(copyUndirectedGraph(tree_2))
    if len(tree_1_center) != len(tree_2_center):
        return False
    if len(tree_1_center) == 1:
        return getAhuRepresentation(tree_1, tree_1_center[0]) == getAhuRepresentation(tree_2, tree_2_center[0])
    else:
        tree_2_rep = getAhuRepresentation(tree_2, tree_2_center[0])
        return getAhuRepresentation(tree_1, tree_1_center[0]) == tree_2_rep or getAhuRepresentation(tree_1, tree_1_center[1]) == tree_2_rep

