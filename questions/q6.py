# Qual o caminho mais curto entre os vértices 4 e 14? 
# Considere os vértices origem e destino como pertencentes ao caminho também.

import networkx as nx

edges_list = [
    (1, 6), 
    (1, 5), 
    (1, 7), 
    (1, 9), 
    (1, 13), 
    (2, 9), 
    (2, 13), 
    (3, 5), 
    (3, 15), 
    (3, 16), 
    (4, 16),
    (4, 15),
    (4, 7),
    (5, 6),
    (5, 17),
    (6, 12),
    (6, 8),
    (7, 8),
    (7, 11),
    (8, 10),
    (8, 17),
    (9, 14),
    (10, 11),
    (12, 14),
    (12, 17)
]

G = nx.Graph()
G.add_edges_from(edges_list)

shortest_path = nx.dijkstra_path(G, source=4, target=14)
print(shortest_path)