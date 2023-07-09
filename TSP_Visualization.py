import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

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
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add Exit button
    exit_button = tk.Button(window, text="Exit", command=close_window)
    exit_button.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Example data
points = np.array([[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]])

# Example tour
tour = [0, 1, 3, 2, 0]

# Create a Tkinter window
window = tk.Tk()
window.title("TSP Visualization")

# Plot the TSP tour
plot_tour(points, tour)
