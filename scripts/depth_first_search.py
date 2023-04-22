import networkx as nx
from typing import Dict, Set, List

DG = nx.DiGraph()

edges_list = [(1, 2), (2, 1), (2, 3), (2, 5), (3, 4), (4, 1), (4, 5), (5, 2)]
DG.add_edges_from(edges_list)
nodes_list: List[int] = DG.nodes

search_start = 1
search_end = 5

covered = set()
queue = [search_start]

neighbors: Dict[int, Set[int]] = {node: set(DG.neighbors(node)) for node in nodes_list}
nodes_sequence_list = list()
predecessors = dict()

while queue:
    actual_node: int = queue[-1]
    node_neighbors: Set[int] = neighbors[actual_node]

    if node_neighbors:
        chosen: int = node_neighbors.pop()
        if chosen not in queue and chosen not in covered:
            queue.append(chosen)
            predecessors[chosen] = actual_node
    else:
        covered.add(actual_node)
        queue.remove(actual_node)
        
actual_node: int = search_end
search_depth = 0
while True:
    nodes_sequence_list.insert(0, actual_node)
    if actual_node == search_start:
        break
    node_predecessor: int = predecessors[actual_node]
    actual_node: int = node_predecessor
    search_depth += 1

nodes_sequence = " --> ".join(map(str, nodes_sequence_list))
print(f'SEARCH FROM {search_start} TO {search_end}: {nodes_sequence}')

print(f'DEPTH SEARCH: {search_depth}')



