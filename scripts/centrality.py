import igraph as ig

g = ig.Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])

# print(g.degree(mode='in'))
# print(g.degree(mode='out'))

# print(g.degree(2))

# print(g.edge_betweenness())


print(g.pagerank(directed=True))