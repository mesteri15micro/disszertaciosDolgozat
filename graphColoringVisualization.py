import networkx as nx
import matplotlib.pyplot as plt

# Function to perform the graph coloring algorithm
def graphColoring(graph):
    coloring = nx.greedy_color(graph, strategy='largest_first')
    return coloring

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (5, 7), (6, 7), (6, 8), (7, 8)])

# Perform graph coloring
coloring = graphColoring(G)

# Get the number of colors used
num_colors = max(coloring.values()) + 1

# Plotting the graph with colors
pos = nx.spring_layout(G)  # Position nodes using spring layout
plt.figure(figsize=(8, 6))

# Draw nodes with different colors
for color in range(num_colors):
    nodes = [node for node, col in coloring.items() if col == color]
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=f"C{color}", node_size=500, alpha=0.8)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color="white")

plt.axis("off")
plt.title("Graph Coloring Visualization")
plt.show()
