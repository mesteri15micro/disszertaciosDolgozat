import sys

def is_safe(v, c, colors):
    for u in adj[v]:
        if u < v and colors[u] == c:
            return False, colors[u]
    return True, colors[v]

def graph_coloring():
    min_colors[0] = sys.maxsize
    stack = [(0, 0)]  # (vertex, level)
    
    while stack:
        v, level = stack.pop()
        
        if v == n:
            max_color = max(colors)
            min_colors[0] = min(min_colors[0], max_color + 1)
            continue
        
        if level < n + 1:
            c = level
            safe, assigned_color = is_safe(v, c, colors)
            if safe:
                colors[v] = c
                stack.append((v, level + 1))
                stack.append((v + 1, 0))
                continue
            else:
                stack.append((v, level + 1))
        
        colors[v] = 0

if __name__ == "__main__":
    # Read input from file
    with open("graphcoloring_rand_10000.in", "r") as fin:
        n, m = map(int, fin.readline().split())
        adj = [[] for _ in range(n)]
        colors = [0] * n
        min_colors = [0]

        for _ in range(m):
            u, v = map(int, fin.readline().split())
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

    # Solve graph coloring problem
    graph_coloring()

    # Store vertex colors
    vertex_colors = list(colors)

    # Write output to file
    with open("graphcoloring_rand_10000.out", "w") as fout:
        # Print colors
        for i in range(n):
            fout.write(f"Vertex {i + 1} is colored {vertex_colors[i]}\n")

        fout.write(f"Number of colors needed: {min_colors[0]}\n")
