from src.dag_algorithms.topological_sort import topSort


def test_topSort():
    dag = [
        [1],
        [2, 3],
        [3],
        []
           ]

    assert topSort(dag) == [0, 1, 2, 3]
