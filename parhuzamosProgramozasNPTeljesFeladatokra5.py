import numpy as np
import multiprocessing
import time

# Function to compute the distance between two points
def compute_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Function to compute the minimum spanning tree
def compute_minimum_spanning_tree(distance_matrix):
    num_vertices = distance_matrix.shape[0]
    visited = [False] * num_vertices
    minimum_spanning_tree = []

    visited[0] = True
    num_visited = 1

    while num_visited < num_vertices:
        min_distance = float('inf')
        min_i, min_j = None, None

        for i in range(num_vertices):
            if visited[i]:
                for j in range(num_vertices):
                    if not visited[j] and distance_matrix[i, j] < min_distance:
                        min_distance = distance_matrix[i, j]
                        min_i, min_j = i, j

        visited[min_j] = True
        minimum_spanning_tree.append((min_i, min_j))
        num_visited += 1

    return minimum_spanning_tree

# Function to find odd degree vertices
def find_odd_degree_vertices(minimum_spanning_tree):
    num_vertices = len(minimum_spanning_tree) + 1
    degree = np.zeros(num_vertices)

    for edge in minimum_spanning_tree:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

    odd_degree_vertices = [v for v in range(num_vertices) if degree[v] % 2 != 0]

    return odd_degree_vertices

# Function to compute the Eulerian circuit
def compute_eulerian_circuit(adjacency_matrix):
    num_vertices = adjacency_matrix.shape[0]
    eulerian_circuit = []
    stack = [0]
    
    while stack:
        v = stack[-1]
        neighbors = np.nonzero(adjacency_matrix[v])[0]

        if len(neighbors) > 0:
            u = neighbors[0]
            stack.append(u)
            adjacency_matrix[v][u] = 0
            adjacency_matrix[u][v] = 0
        else:
            eulerian_circuit.append(stack.pop())

    return eulerian_circuit

# Function to compute the TSP tour using the Christofides algorithm
def christofides(points):
    num_vertices = len(points)
    distance_matrix = np.zeros((num_vertices, num_vertices))

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance_matrix[i, j] = compute_distance(points[i], points[j])
            distance_matrix[j, i] = distance_matrix[i, j]

    minimum_spanning_tree = compute_minimum_spanning_tree(distance_matrix)
    odd_degree_vertices = find_odd_degree_vertices(minimum_spanning_tree)

    adjacency_matrix = np.zeros((num_vertices, num_vertices))

    for edge in minimum_spanning_tree:
        adjacency_matrix[edge[0]][edge[1]] = 1
        adjacency_matrix[edge[1]][edge[0]] = 1

    for v in odd_degree_vertices:
        min_distance = float('inf')
        min_neighbor = None

        for u in range(num_vertices):
            if u != v and (min_neighbor is None or distance_matrix[v, u] < min_distance):
                min_distance = distance_matrix[v, u]
                min_neighbor = u

        adjacency_matrix[v][min_neighbor] = 1
        adjacency_matrix[min_neighbor][v] = 1

    eulerian_circuit = compute_eulerian_circuit(adjacency_matrix)
    visited = [False] * num_vertices
    tsp_tour = []

    for v in eulerian_circuit:
        if not visited[v]:
            tsp_tour.append(v)
            visited[v] = True

    tsp_tour.append(tsp_tour[0])  # Complete the tour

    return tsp_tour

# Function to perform bin packing
def bin_packing(items, bin_capacity):
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
            newBin = {'capacity': bin_capacity, 'items': [item]}
            bins.append(newBin)
    return bins

# Function to solve TSP and bin packing problems in parallel
def tsp_bin_packing_parallel(points, bin_capacity):
    num_items = len(points)  # Update num_items to the correct value

    # Solve TSP problem using Christofides algorithm
    start_tsp = time.time()
    tsp_tour = christofides(points)
    end_tsp = time.time()

    # Divide items into chunks for parallel processing
    num_processes = multiprocessing.cpu_count()
    chunk_size = (num_items + num_processes - 1) // num_processes  # Calculate chunk size

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Perform bin packing in parallel
    start_bin_packing = time.time()
    results = pool.starmap(bin_packing, [(points[i:i+chunk_size], bin_capacity) for i in range(0, num_items, chunk_size)])
    end_bin_packing = time.time()

    # Concatenate the results
    bin_packing_results = np.concatenate(results)

    tsp_time = end_tsp - start_tsp
    bin_packing_time = end_bin_packing - start_bin_packing

    return tsp_tour, bin_packing_results, tsp_time, bin_packing_time

# Example usage
if __name__ == "__main__":
    points = [[0, 0], [1, 3], [2, 1], [4, 2], [3, 0]]
    bin_capacity = 5

    start_total = time.time()
    tsp_tour, bin_packing_results, tsp_time, bin_packing_time = tsp_bin_packing_parallel(points, bin_capacity)
    end_total = time.time()

    print("TSP Tour:", tsp_tour)
    print("Bin Packing Results:", bin_packing_results)
    print("TSP Time:", tsp_time, "seconds")
    print("Bin Packing Time:", bin_packing_time, "seconds")
    print("Total Time:", end_total - start_total, "seconds")
