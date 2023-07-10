from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import io
import base64

app = Flask(__name__)

def plot_tour(points, tour):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(points[:, 0], points[:, 1], color='blue', s=50)
    ax.plot(points[tour + [tour[0]], 0], points[tour + [tour[0]], 1], color='red', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Christofides Algorithm Tour')
    ax.grid(True)

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
    points = np.array([[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]])
    tour = [0, 1, 3, 2, 0]
    plot_data = plot_tour(points, tour)
    return render_template('cristofides_visualization.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)