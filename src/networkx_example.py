# import pandas as pd
# import numpy as np

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(2, 3)
G.add_edge(1, 3)
G.add_edge(1, 2)
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')