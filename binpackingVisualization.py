import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

# Generate random item sizes
items = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Set bin capacity
binCapacity = 50

# Perform binpacking
bins = binPacking(items, binCapacity)

# Create a Tkinter window
window = tk.Tk()
window.title("Binpacking Visualization")

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

# Create a canvas to display the matplotlib figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Add Exit button
exit_button = tk.Button(window, text="Exit", command=close_window)
exit_button.pack()

# Start the Tkinter event loop
window.mainloop()
