from src.tree_algorithms.center import findCenter


def test_center():
    tree = {
        1: [2],
        2: [1, 3, 4],
        3: [2],
        4: [2]
        }

    bicentral_tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
    }

    assert findCenter(tree)[0] == 2
    assert findCenter(bicentral_tree)[0] == 2
    assert findCenter(bicentral_tree)[1] == 3
