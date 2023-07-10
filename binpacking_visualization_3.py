from flask import Flask, render_template, jsonify

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
    return render_template('visualization.html')

# Route to provide the algorithm data as JSON
@app.route('/data')
def data():
    return jsonify(bins)

if __name__ == '__main__':
    app.run(debug=True)