from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import networkx as nx
import io
import base64

app = Flask(__name__)

def graphColoringVisualization():
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

    # Create the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw nodes with different colors
    for color in range(num_colors):
        nodes = [node for node, col in coloring.items() if col == color]
        nx.draw_networkx_nodes(G, pos=layout, nodelist=nodes, node_color=f"C{color}", ax=ax)

    # Draw edges
    nx.draw_networkx_edges(G, pos=layout, ax=ax)

    # Set the axis off
    ax.set_axis_off()

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)
    buffer.seek(0)

    # Encode the bytes buffer as a base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return plot_data

@app.route('/')
def index():
    plot_data = graphColoringVisualization()
    return render_template('graph_coloring_visualization.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)