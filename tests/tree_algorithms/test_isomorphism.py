from src.tree_algorithms.isomorphism import getAhuRepresentation, areIsomorphic


def test_getAhuRepresentation():
    tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
    }

    assert getAhuRepresentation(tree, 2) == '((()())())'
    assert getAhuRepresentation(tree, 3) == '((())()())'


def test_areIsomorphic():
    tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
    }

    tree_2 = {
        1: [3],
        2: [3],
        3: [1, 2, 4],
        4: [5, 3],
        5: [4]
    }

    tree_3 = {
        1: [2],
        2: [1]
    }

    tree_4 = {
        1: [4],
        2: [4],
        3: [4],
        4: [1, 2, 3]
    }

    tree_5 = {
        1: [2, 3, 4],
        2: [1],
        3: [1],
        4: [1]
    }

    assert areIsomorphic(tree, tree_2)
    assert not areIsomorphic(tree, tree_3)
    assert areIsomorphic(tree_4, tree_5)
