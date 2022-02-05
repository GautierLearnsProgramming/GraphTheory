import src.tree_algorithms.utils


def test_delete_node():
    tree = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }

    src.tree_algorithms.utils.deleteNode(tree, 1)
    assert len(tree[2]) == 1
    assert len(tree[3]) == 0
