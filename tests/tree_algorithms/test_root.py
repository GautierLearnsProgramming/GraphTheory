from src.tree_algorithms.root import rootTree


def test_rootTree():
    tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
    }

    rooted_tree_1 = rootTree(tree, 1)
    rooted_tree_2 = rootTree(tree, 2)
    rooted_tree_3 = rootTree(tree, 3)

    assert rooted_tree_1[1] == [2]
    assert rooted_tree_1[2] == [3]
    assert rooted_tree_1[3] == [4, 5]
    assert rooted_tree_1[4] == []
    assert rooted_tree_1[5] == []

    assert rooted_tree_2[1] == []
    assert rooted_tree_2[2] == [1, 3]
    assert rooted_tree_2[3] == [4, 5]
    assert rooted_tree_2[4] == []
    assert rooted_tree_2[5] == []

    assert rooted_tree_3[1] == []
    assert rooted_tree_3[2] == [1]
    assert rooted_tree_3[3] == [2, 4, 5]
    assert rooted_tree_3[4] == []
    assert rooted_tree_3[5] == []
