import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Function to close the window
def close_window():
    window.destroy()

    # Close the matplotlib figure
    plt.close(fig)

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

# Save the layout before graph coloring
layout = nx.spring_layout(G)

# Perform graph coloring
coloring = graphColoring(G)

# Get the number of colors used
num_colors = max(coloring.values()) + 1

# Create a Tkinter window
window = tk.Tk()
window.title("Graph Coloring Visualization")

# Create a matplotlib figure
fig, ax = plt.subplots(figsize=(8, 6))

# Draw nodes with different colors
for color in range(num_colors):
    nodes = [node for node, col in coloring.items() if col == color]
    nx.draw_networkx_nodes(G, pos=layout, nodelist=nodes, node_color=f"C{color}", ax=ax)

# Draw edges
nx.draw_networkx_edges(G, pos=layout, ax=ax)

# Set the axis off
ax.set_axis_off()

# Create a canvas to display the matplotlib figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Add Exit button
exit_button = tk.Button(window, text="Exit", command=close_window)
exit_button.pack()

# Start the Tkinter event loop
window.mainloop()
