from src.visualization.visualize import visualize

tree = {
        1: [2],
        2: [1, 3],
        3: [2, 4, 5],
        4: [3],
        5: [3]
        }

visualize("newviz", tree)
