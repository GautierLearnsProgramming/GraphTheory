from src.visualization.visualize import visualize

tree = {1: [2],
        2: [1, 3, 4],
        3: [2],
        4: [2]
        }

visualize("newviz", tree)
