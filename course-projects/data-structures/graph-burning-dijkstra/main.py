import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import string

n = int(input("Please enter the number of nodes: "))
G = nx.Graph()
nodes = list(string.ascii_uppercase[:n])
G.add_nodes_from(nodes)


weights_adjMatrix = []
for i in range(n):
    rows = []
    for j in range(n):
        if i < j:
            weight = int(input(f"Please enter the weight from {i} to {j}: ")) 
            rows.append(weight)
        else:
            rows.append(0)
    weights_adjMatrix.append(rows)

weights_adjMatrix = np.array(weights_adjMatrix)
np.fill_diagonal(weights_adjMatrix, 0)


for i in range(n):
    for j in range(n):
        if i != j and weights_adjMatrix[i, j] != 0:  
            G.add_edge(nodes[i], nodes[j], weight=weights_adjMatrix[i, j])


source_node_index = int(input("Please enter the index of the source node: "))
source_node = nodes[source_node_index]

shortest_path = nx.single_source_dijkstra_path(G, source_node, weight='weight')
for target, path in shortest_path.items():
    if target != source_node:  
        print(f"Shortest path from {source_node} to {target}: {path}")
 

def burning_centers(G):
    remaining_nodes = set(G.nodes())  
    burning_centers = []  
    while remaining_nodes:
        max_degree_node = max(remaining_nodes, key=lambda x: G.degree(x))
        burning_centers.append(max_degree_node)
        remaining_nodes.remove(max_degree_node)
        burned_nodes = {max_degree_node}
        for _ in range(len(burning_centers)):
            next_burned_nodes = set()
            for node in burned_nodes:
                next_burned_nodes.update(set(G.neighbors(node)) & remaining_nodes)
            burned_nodes = next_burned_nodes
            remaining_nodes -= burned_nodes
    burning_number = len(burning_centers)
    return burning_number, burning_centers
burning_number, sequence = burning_centers(G)
print("Burning number:", burning_number)
print("Burning sequences:", sequence)


pos = nx.shell_layout(G)  
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

