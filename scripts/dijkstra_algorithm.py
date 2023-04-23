import networkx as nx
from typing import Dict, List

DG = nx.DiGraph()

edges_list = [(1, 2, 1.0), (2, 1, 3.0), (2, 3, 1.0), (2, 5, 1.0), (3, 4, 2.0), (4, 1, 5.0), (4, 5, 1.0), (5, 2, 2.0)]
DG.add_weighted_edges_from(edges_list)

nodes_list: List[int] = DG.nodes
edges = DG.edges
neighbors: Dict[int, List[int]] = {node: list(DG.neighbors(node)) for node in nodes_list}

search_start = 5
search_end = 2

covered = set()
breadths = dict()
predecessors = dict()


actual_node = search_start
covered.add(search_start)
length = 0
while len(covered) < len(nodes_list):
    node_neighbors: List[int] = [node for node in neighbors[actual_node] if node not in covered]
    distances: List[float] = [edges[actual_node, node]["weight"] for node in node_neighbors if node not in covered]

    for node_index, distance in enumerate(distances):
        node = node_neighbors[node_index]
        breadths[node] = distance + length
        predecessors[node] = actual_node
        covered.add(node)

    if distances:
        min_distance = min(distances)
        nearest_node: int = node_neighbors[distances.index(min_distance)]
        actual_node: int = nearest_node
        length: float = min_distance + length


actual_node = search_end
path = list()
while True:
    path.insert(0, actual_node)
    if actual_node == search_start:
        break
    actual_node = predecessors[actual_node]


print(f'Path: {path}')


    


