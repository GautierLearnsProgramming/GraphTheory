from typing import Union


# The root tree function takes a tree as input and returns a rooted tree (i.e, edges are no longer undirected)
def rootTree(tree: dict[int, list[int]], root_index: int) -> dict[int, list[int]]:
    rooted_tree: dict[int, list[int]] = {}
    buildTree(tree, rooted_tree, root_index, None)
    return rooted_tree


def buildTree(tree: dict[int, list[int]], rootedTree: dict[int, list[int]], node_index: int, parent_index: Union[int, None]):
    # The build tree is the recursive call back in the depth-first traversal of the base tree.
    node_children = [child_index for child_index in tree[node_index] if child_index != parent_index]
    rootedTree.update({node_index: node_children})
    for child_index in node_children:
        buildTree(tree, rootedTree, child_index, node_index)
