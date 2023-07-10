from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64
import numpy as np

app = Flask(__name__)

def tspVisualization():
    # Function to close the window
    def close_window():
        window.destroy()
        # Close the matplotlib figure
        plt.close(fig)

    # Function to plot the TSP tour
    def plot_tour(points, tour):
        global fig  # Declare fig as a global variable

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(points[:, 0], points[:, 1], color='blue', s=50)
        ax.plot(points[tour + [tour[0]], 0], points[tour + [tour[0]], 1], color='red', linewidth=2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('TSP Tour')
        ax.grid(True)

        # Create a canvas to display the matplotlib figure in the Tkinter window
        canvas = FigureCanvas(fig)
        canvas.draw()

        # Save the plot to a bytes buffer
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)

        # Encode the bytes buffer as a base64 string
        plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return plot_data

    # Example data
    points = np.array([[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]])

    # Example tour
    tour = [0, 1, 3, 2, 0]

    plot_data = plot_tour(points, tour)

    return plot_data

@app.route('/')
def index():
    plot_data = tspVisualization()
    return render_template('tsp_visualization.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)