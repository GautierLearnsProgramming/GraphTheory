from typing import Union
import graphviz


def visualize(output_file: str, graph: Union[dict[int, list[int]], dict[int, list[tuple[int, float]]]], directed: bool = False, weighted: bool = False):
    dot = graphviz.Digraph()
    if not directed:
        dot = graphviz.Graph()
    for node_index, node_edges in graph.items():
        dot.node(str(node_index))
        for edge in node_edges:
            # In the case of an undirected graph, where each node appears twice, we skip one rendering
            if not directed:
                if weighted:
                    if node_index > edge[0]:
                        continue
                else:
                    if node_index > edge:
                        continue
            if weighted:
                dot.edge(str(node_index), str(edge[0]), str(edge[1]))
            else:
                dot.edge(str(node_index), str(edge))
    dot.render(f'doctest-output/{output_file}.gv').replace('\\', '/')
