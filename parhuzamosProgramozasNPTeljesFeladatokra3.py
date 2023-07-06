import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# Function to close the window
def close_window():
    window.destroy()
    # Close the matplotlib figure
    plt.close(fig)

# Function to perform the binpacking algorithm
def binPacking(items, binCapacity):
    bins = []
    items.sort(reverse=True)
    for item in items:
        added = False
        for bin in bins:
            if bin['capacity'] >= item:
                bin['items'].append(item)
                bin['capacity'] -= item
                added = True
                break
        if not added:
            newBin = {'capacity': binCapacity, 'items': [item]}
            bins.append(newBin)
    return bins

# Function to perform the knapsack algorithm
def knapsack(items, capacity):
    num_items = len(items)
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the selected items
    selected_items = []
    i, j = num_items, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1][0]
        i -= 1

    return dp[num_items][capacity], selected_items[::-1]

# Function to perform the Christofides algorithm
def christofides(points):
    graph = nx.Graph()
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = np.linalg.norm(points[i] - points[j])
            graph.add_edge(i, j, weight=distance)
    
    mst = nx.minimum_spanning_tree(graph)
    odd_nodes = [node for node, degree in mst.degree() if degree % 2 != 0]
    perfect_matching = nx.algorithms.max_weight_matching(mst, weight='weight', maxcardinality=True)
    eulerian_graph = nx.MultiGraph(mst)
    for u, v in perfect_matching:
        eulerian_graph.add_edge(u, v, weight=nx.dijkstra_path_length(graph, u, v))
    eulerian_path = list(nx.eulerian_circuit(eulerian_graph))

    tour = [eulerian_path[0][0]]
    for edge in eulerian_path:
        if edge[1] not in tour:
            tour.append(edge[1])

    return tour

# Function to perform the graph coloring algorithm
def graphColoring(graph):
    coloring = nx.greedy_color(graph, strategy='largest_first')
    return coloring

# Function to find the Hamiltonian cycle
def findHamiltonianCycle(graph):
    try:
        cycle = nx.find_cycle(graph, orientation='original')
        return [node for node, _ in cycle]
    except nx.NetworkXNoCycle:
        return None

# Create a sample window
window = tk.Tk()
window.title("Python Algorithms Visualization")
window.geometry("800x600")

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])

# Perform bin packing algorithm
items = [5, 7, 10, 4, 2, 6, 9]
bin_capacity = 15
bins = binPacking(items, bin_capacity)

# Perform knapsack algorithm
knapsack_items = [(2, 5), (4, 8), (3, 6), (5, 10), (6, 12)]
knapsack_capacity = 10
max_value, selected_items = knapsack(knapsack_items, knapsack_capacity)

# Perform Christofides algorithm
points = np.array([[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]])
christofides_tour = christofides(points)

# Perform graph coloring algorithm
coloring_graph = nx.Graph()
coloring_graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
graph_coloring = graphColoring(coloring_graph)

# Find Hamiltonian cycle in the graph
hamiltonian_graph = nx.Graph()
hamiltonian_graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
hamiltonian_cycle = findHamiltonianCycle(hamiltonian_graph)

# Create a matplotlib figure
fig = plt.figure(figsize=(6, 4))

# Plot the graph
ax1 = fig.add_subplot(231)
nx.draw_networkx(G, with_labels=True, ax=ax1)

# Plot the bin packing result
ax2 = fig.add_subplot(232)
ax2.set_title("Bin Packing")
for i, bin in enumerate(bins):
    ax2.barh(i, sum(bin['items']), align='center')
ax2.set_xlabel("Bin Capacity")
ax2.set_ylabel("Bins")

# Plot the knapsack result
ax3 = fig.add_subplot(233)
ax3.set_title("Knapsack")
ax3.barh(range(len(selected_items)), [item[1] for item in selected_items], align='center')
ax3.set_yticks(range(len(selected_items)))
ax3.set_yticklabels([f"Item {i+1}" for i in range(len(selected_items))])
ax3.set_xlabel("Value")
ax3.set_ylabel("Items")

# Plot the Christofides result
ax4 = fig.add_subplot(234)
ax4.set_title("Christofides Algorithm")
ax4.plot(points[christofides_tour][:, 0], points[christofides_tour][:, 1], 'o-')
ax4.set_xlabel("X")
ax4.set_ylabel("Y")

# Plot the graph coloring result
ax5 = fig.add_subplot(235)
ax5.set_title("Graph Coloring")
nx.draw_networkx(coloring_graph, node_color=list(graph_coloring.values()), with_labels=True, ax=ax5)

# Plot the Hamiltonian cycle
ax6 = fig.add_subplot(236)
ax6.set_title("Hamiltonian Cycle")
if hamiltonian_cycle:
    hamiltonian_graph.add_edge(hamiltonian_cycle[-1], hamiltonian_cycle[0])
    nx.draw_networkx(hamiltonian_graph, with_labels=True, ax=ax6)
else:
    ax6.text(0.5, 0.5, "No Hamiltonian Cycle", ha='center', va='center')

# Create a Tkinter canvas for the matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Add a button to close the window
button = tk.Button(window, text="Close", command=close_window)
button.pack()

# Run the Tkinter event loop
window.mainloop()
