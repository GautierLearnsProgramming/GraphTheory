from adj_list_rep.adjacency_list import AdjacencyList
from adj_list_rep.graphs import gen_tree, gen_random_graph
import graphviz
from algorithms.dfs import dfs, bfs

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tree = gen_tree(17, 3)
tree.visualize('tree')

# directed = gen_random_graph(13, mean_edges=2, std_dev_edges=2, weighted=True, mean_weight=3, std_dev_weight=2)
# directed.visualize("directed")
#
# undirected = gen_random_graph(20, mean_edges=2, std_dev_edges=2, weighted=False, directed=False)
# undirected.visualize("undirected")

print('dfs')
dfs(tree)
print('bfs')
bfs(tree)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Goals : adjacency list representation, adjacency matrix representations
