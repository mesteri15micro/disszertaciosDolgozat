import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

# Define the figure and canvas globally
fig = None
canvas = None

# Function to close the window
def close_window():
    window.destroy()

    # Close the matplotlib figure and canvas if they exist
    if fig is not None:
        plt.close(fig)
    if canvas is not None:
        canvas.get_tk_widget().destroy()

# Function to plot the Hamiltonian cycle
def plot_hamiltonian_cycle(graph, cycle):
    global fig, canvas

    # Create a subgraph with only the nodes and edges of the Hamiltonian cycle
    cycle_edges = [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)] + [(cycle[-1], cycle[0])]
    subgraph = graph.subgraph(cycle + cycle_edges)

    fig, ax = plt.subplots(figsize=(6, 6))
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos=pos, ax=ax)
    nx.draw_networkx_edges(subgraph, pos=pos, edgelist=cycle_edges, edge_color='r', width=2)
    ax.set_axis_off()

    # Create a new canvas to display the matplotlib figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add Exit button
    exit_button = tk.Button(window, text="Exit", command=close_window)
    exit_button.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 1)])

# Create a Tkinter window
window = tk.Tk()
window.title("Hamiltonian Circle Visualization")

# Plot the Hamiltonian cycle
plot_hamiltonian_cycle(G, [1, 2, 4, 3, 5])
