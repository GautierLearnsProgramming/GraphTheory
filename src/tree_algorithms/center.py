# Delete a node in an undirected graph
from src.tree_algorithms.utils import deleteNode, copyUndirectedGraph


# Find center returns a list containing one or two integers representing the indexes of the center of the two centers
# The tree is assumed to be UNDIRECTED, which means that any edge (u,v) has a corresponding edge (v,u)
def findCenter(tree: dict[int, list[int]]) -> list[int]:
    # Algorithm structure :
    # Step 1 : Compute the degree of every node in the graph
    # Step 2 : Prune every leaf node whose degree is 1
    # Step 3 : Repeat step 2 with the new degrees until only one or two nodes are left
    tree = copyUndirectedGraph(tree)
    degreesDict: dict[int, int] = {}
    nodesToRemove: list[int] = []

    # Compute all of the tree's degrees and add nodes of degree one to the remove list
    for node_index, neighbors in tree.items():
        degree = len(neighbors)
        degreesDict[node_index] = degree
        if degree == 1:
            nodesToRemove.append(node_index)

    while len(tree.keys()) > 2:
        nodesToRemoveCopy = [node for node in nodesToRemove]
        nodesToRemove.clear()
        # Go through the list of nodes of degree 1 that we want to remove
        # For each node in the list, update its neighbors indexes (decrease it by one), and if the neighbor is now
        # of degree, ad it to the list of nodes to remove at the next iteration
        for node_index in nodesToRemoveCopy:
            for neighbor_index in tree[node_index]:
                neighbor_new_degree = degreesDict[neighbor_index] - 1
                degreesDict[neighbor_index] = neighbor_new_degree
                if neighbor_new_degree == 1:
                    nodesToRemove.append(neighbor_index)
            deleteNode(tree, node_index)
    return [node_index for node_index in tree.keys()]

