import numpy as np
import matplotlib.pyplot as plt

# Function to plot the Christofides algorithm tour
def plot_tour(points, tour):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], color='blue', s=50)
    plt.plot(points[tour + [tour[0]], 0], points[tour + [tour[0]], 1], color='red', linewidth=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Christofides Algorithm Tour')
    plt.grid(True)
    plt.show()

# Example data
points = np.array([[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]])

# Example tour
tour = [0, 1, 3, 2, 0]

# Plot the Christofides algorithm tour
plot_tour(points, tour)
