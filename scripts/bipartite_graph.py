import igraph as ig
import matplotlib.pyplot as plt


g = ig.Graph(
    9,
    [(0, 4), (0, 5), (1, 4), (1, 6), (1, 7), (2, 5), (2, 7), (2, 8), (3, 6), (3, 7)],
    directed=True
    )

g.vs[range(4)]["type"] = True
g.vs[range(4, 9)]["type"] = False

layout = g.layout_bipartite()
one, other = g.bipartite_projection()

fig, ax = plt.subplots()
ig.plot(
    one,
    target=ax,
    vertex_label=g.vs.indices,
    layout=layout
    )

plt.show()

