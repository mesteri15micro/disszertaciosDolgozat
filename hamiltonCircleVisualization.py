import networkx as nx
import matplotlib.pyplot as plt

# Function to perform the Hamiltonian cycle algorithm
def hamiltonianCycle(graph):
    cycle = nx.find_cycle(graph)
    return cycle

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (5, 7), (6, 7), (6, 8), (7, 8)])

# Perform Hamiltonian cycle
cycle = hamiltonianCycle(G)

# Plotting the graph with Hamiltonian cycle
pos = nx.spring_layout(G)  # Position nodes using spring layout
plt.figure(figsize=(8, 6))

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw nodes with different colors
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500, alpha=0.8)

# Draw Hamiltonian cycle edges
edges = list(cycle)
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2.0, alpha=1.0)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color="white")

plt.axis("off")
plt.title("Hamiltonian Cycle Visualization")
plt.show()
