from src.tree_algorithms import graph


def test_delete_node():
    tree = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }

    graph.deleteNode(tree, 1)
    assert len(tree[2]) == 1
    assert len(tree[3]) == 0
