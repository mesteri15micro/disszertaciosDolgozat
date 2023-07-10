from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

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

# Generate random item sizes
items = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Set bin capacity
binCapacity = 50

# Perform binpacking
bins = binPacking(items, binCapacity)

# Route to render the visualization template
@app.route('/')
def index():
    # Create a matplotlib figure
    fig, ax = plt.subplots()
    ax.set_title('Binpacking Visualization')
    ax.set_xlabel('Bin')
    ax.set_ylabel('Item Size')

    # Plot each bin
    for i, bin in enumerate(bins):
        y = [i+1] * len(bin['items'])
        x = [j+1 for j in range(len(bin['items']))]
        ax.scatter(x, y, marker='s', s=200, color='blue')
        for j, item in enumerate(bin['items']):
            ax.annotate(item, (x[j], y[j]), ha='center', va='center')

    # Set the y-axis limit
    ax.set_ylim(0.5, len(bins) + 0.5)

    # Convert the matplotlib figure to an image buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    data = base64.b64encode(buf.read()).decode()

    # Close the matplotlib figure
    plt.close(fig)

    # Render the template and pass the base64-encoded image data
    return render_template('visualization.html', image_data=data)

# Route to provide the algorithm data as JSON
@app.route('/data')
def data():
    return jsonify(bins)

if __name__ == '__main__':
    app.run(debug=True)