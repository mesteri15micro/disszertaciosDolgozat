import sys
import time

def is_safe(v, c, colors):
    for u in adj[v]:
        if u < v and colors[u] == c:
            return False, colors[u]
    return True, colors[v]

def graph_coloring_util(v, colors):
    if v == n:
        max_color = max(colors)
        min_colors[0] = min(min_colors[0], max_color + 1)
        return

    for c in range(n + 1):
        safe, assigned_color = is_safe(v, c, colors)
        if safe:
            colors[v] = c
            graph_coloring_util(v + 1, colors)
            return assigned_color
    
    colors[v] = 0

def graph_coloring():
    min_colors[0] = sys.maxsize
    start_time = time.time()
    graph_coloring_util(0, colors)
    end_time = time.time()
    return min_colors[0], end_time - start_time

if __name__ == "__main__":
    # Read input from file
    with open("graphcoloring1000.in", "r") as fin:
        n, m = map(int, fin.readline().split())
        adj = [[] for _ in range(n)]
        colors = [0] * n
        min_colors = [0]

        for _ in range(m):
            u, v = map(int, fin.readline().split())
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

    # Solve graph coloring problem and measure execution time
    num_colors, execution_time = graph_coloring()

    # Store vertex colors
    vertex_colors = list(colors)

    # Write output to file
    with open("graphcoloring1000.out", "w") as fout:
        # Print colors
        for i in range(n):
            fout.write(f"Vertex {i + 1} is colored {vertex_colors[i]}\n")

        fout.write(f"Number of colors needed: {num_colors}\n")
        fout.write(f"Execution time: {execution_time} seconds\n")
