import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to close the window
def close_window():
    window.destroy()

    # Close the matplotlib figure
    plt.close(fig)

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

# Example items
items = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10)]

# Example knapsack capacity
capacity = 20

# Solve the knapsack problem
max_value, selected_items = knapsack(items, capacity)

# Create a Tkinter window
window = tk.Tk()
window.title("Knapsack Visualization")

# Create a matplotlib figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the knapsack items
for item in items:
    ax.scatter(item[0], item[1], color='blue', s=50)
ax.set_xlabel('Weight')
ax.set_ylabel('Value')
ax.set_title('Knapsack Visualization')
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
