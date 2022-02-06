from src.visualization.visualize import visualize
from src.tree_algorithms.root import rootTree
from src.tree_algorithms.utils import copyUndirectedGraph
from src.tree_algorithms.center import findCenter
from src.tree_algorithms.isomorphism import rootedTreeToTreeWithParent, getAhuRepresentation
from src.dag_algorithms.topological_sort import topSort

tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
        }

dag = [
        [1],
        [2, 3],
        [3],
        []
        ]

print(topSort(dag))
