from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import networkx as nx
import io
import base64

app = Flask(__name__)

def hamiltonCircleVisualization():
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
        nonlocal fig, canvas

        # Create a subgraph with only the nodes and edges of the Hamiltonian cycle
        cycle_edges = [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)] + [(cycle[-1], cycle[0])]
        subgraph = graph.subgraph(cycle + cycle_edges)

        fig, ax = plt.subplots(figsize=(6, 6))
        pos = nx.spring_layout(graph)
        nx.draw_networkx(graph, pos=pos, ax=ax)
        nx.draw_networkx_edges(subgraph, pos=pos, edgelist=cycle_edges, edge_color='r', width=2)
        ax.set_axis_off()

        # Save the plot to a bytes buffer
        buffer = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buffer)
        buffer.seek(0)

        # Encode the bytes buffer as a base64 string
        plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return plot_data

    # Create a graph
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from([1, 2, 3, 4, 5])

    # Add edges to the graph
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 1)])

    plot_data = plot_hamiltonian_cycle(G, [1, 2, 4, 3, 5])

    return plot_data

@app.route('/')
def index():
    plot_data = hamiltonCircleVisualization()
    return render_template('hamilton_circle_visualization.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)