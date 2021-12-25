from adj_list_rep.adjacency_list import AdjacencyList
from adj_list_rep.edge import Edge
from random import random, randint


def random_float(mean: float, std_dev: float):
    m = mean
    v = (random() - 0.5) * 2 * std_dev
    return m + v


def gen_tree(size: int, children_mean: float = 0, children_std_dev=2) -> AdjacencyList:
    if children_mean == 0:
        children_mean = size // 5 + 1

    depth = 0
    layer_connected = False
    depth_array = [0 for i in range(size)]

    tree = AdjacencyList(False, False)
    hasParentIndex = 1
    rootingIndex = 0
    for i in range(size):
        tree.vertex()
    while hasParentIndex < size:
        # Make sure at least one node goes from the current layer to the next one
        child_nodes = round(random_float(children_mean, children_std_dev))
        if not layer_connected:
            child_nodes = max(1, child_nodes)
            layer_connected = True
        for i in range(child_nodes):
            # Create an edge from the current rooting node to a child
            tree.edge(rootingIndex, hasParentIndex)
            depth_array[hasParentIndex] = depth + 1
            hasParentIndex += 1
            if hasParentIndex >= size:
                break
        rootingIndex += 1
        # Increment depth if necessary, and reset layer_connected if we moved down a layer
        if depth_array[rootingIndex] > depth:
            layer_connected = False
            depth = depth_array[rootingIndex]
    return tree


# What should the gen_random_graph function do ?
# generate a random graph ! what possibilities should it have ?
# Generate a graph of any size
# Directed or undirected graph
# Weighted or unweighted graph
# Sparse or dense graph -> specify the average number of edges going from any given node
# If weighted, be able to specify the distribution of the weights (mean, standard deviation)
def gen_random_graph(size: int = 25, mean_edges: float = 5, std_dev_edges: float = 5, directed: bool = True,
                     weighted: bool = False, mean_weight: float = 5, std_dev_weight: float = 4,
                     allow_self_edge: bool = False) -> AdjacencyList:
    graph = AdjacencyList(directed, weighted)

    for i in range(size):
        graph.vertex()

    for i in range(size):
        # Generate the number of edges for the node (halve it in the case of undirected graphs because each edge
        # generates an additional one)
        new_edges_count = random_float(mean_edges, std_dev_edges)
        if not directed:
            new_edges_count /= 2
        new_edges_count = round(new_edges_count)
        # For each edge, generate a random weight
        for j in range(new_edges_count):
            # Generate a random int for the child node
            edge_target = randint(0, size - 1)
            edge = Edge(i, edge_target, 1)
            # generate a new target if the node target it self and self-targeting is disallowed
            if not allow_self_edge:
                if edge.u == edge.v:
                    j -= 1
                    continue
            # if the node already has an edge going to the target, generate a new target
            if any((e.u == edge.u and e.v == edge.v) for e in graph.vertices[edge.u].edges):
                j -= 1
                continue
            # If we want a weighted graph, generate a random weight for the edge
            if weighted:
                weight = round(random_float(mean_weight, std_dev_weight))
                edge.w = weight
            if directed:
                graph.add_edge(edge)
            else:
                graph.edge(edge.u, edge.v, edge.w)
                graph.edge(edge.v, edge.u, edge.w)
    return graph
