import networkx as nx
from typing import Dict, Set, List

DG = nx.DiGraph()

edges_list = [(1, 2), (2, 1), (2, 3), (2, 5), (3, 4), (4, 1), (4, 5), (5, 2)]
DG.add_edges_from(edges_list)

search_start = 1
search_end = 5

fifo = [search_start]
covered = set()
breadths = dict()

nodes_list: List[int] = DG.nodes

neighbors: Dict[int, Set[int]] = {node: set(DG.neighbors(node)) for node in nodes_list}

node_predecessor = dict()

#print(neighbors)
	
while fifo:
    actual_node = fifo[0]
    predecessor = node_predecessor.get(actual_node)

    breadths[actual_node] = 1 + breadths.get(predecessor, -1)
    covered.add(fifo.pop(0))

    for neighbor in neighbors[actual_node]:
        if neighbor not in covered:
            fifo.append(neighbor)
            node_predecessor[neighbor] = actual_node

#print(breadths)
#print(covered)

#print(node_predecessor)

actual_node = search_end
path = list()
while True:
    path.insert(0, str(actual_node))

    if actual_node == search_start:
        break
    actual_node = node_predecessor[actual_node]

print("path:", " -> ".join(path))
 


