from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route('/')
def index():
    items = [5, 3, 1, 2, 4]  # Replace with your data or modify as needed

    # Perform sorting or any other necessary operations
    items_sorted = sorted(items)

    return render_template('index.html', items=items_sorted)

if __name__ == '__main__':
    app.run(debug=True)