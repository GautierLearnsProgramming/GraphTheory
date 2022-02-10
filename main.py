from src.visualization.visualize import visualize
from src.sssp_algorithms.dijkstra import dijkstra_lazy
import src.graph_utils.conversion as conversion

adj_map = {
        0: [(1, 1), (2, 1)],
        1: [(3, 3), (4, 2)],
        2: [(3, 1)],
        3: [],
        4: []
}

visualize("dijkstra", adj_map, weighted=True, directed=True)

adj_list, list_to_map = conversion.weighted_adj_map_to_adj_list(adj_map)

print(dijkstra_lazy(adj_list, 0))
print(dijkstra_lazy(adj_list, 1))
