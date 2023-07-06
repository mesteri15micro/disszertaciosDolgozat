#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <unordered_set>
#include <chrono>

const int MAXN = 10100; // Maximum number of vertices

int n; // Number of vertices
std::vector<int> adj[MAXN]; // Adjacency list of the graph
int color[MAXN]; // Array of vertex colors

bool isSafe(int v, int c) {
    for (int i = 0; i < adj[v].size(); ++i) {
        int u = adj[v][i];
        if (color[u] == c) {
            return false;
        }
    }
    return true;
}

bool graphColoringUtil(int v) {
    if (v == n + 1) {
        return true;
    }

    for (int c = 1; c <= n; ++c) {
        if (isSafe(v, c)) {
            color[v] = c;
            if (graphColoringUtil(v + 1)) {
                return true;
            }
            color[v] = 0; // backtrack
        }
    }

    return false;
}

int getColorCount() {
    std::unordered_set<int> colorSet;
    for (int i = 1; i <= n; i++) {
        colorSet.insert(color[i]);
    }
    return colorSet.size();
}

int main() {
    std::ifstream fin("graphcoloring_rand_10000.in");
    std::ofstream fout("graphcoloring_rand_10000.out");

    double elapsedTime;
    // Read input
    int m; // Number of edges
    fin >> n >> m;
    std::cout << "n=" << n << "\t\tm=" << m << "\n";
    for (int i = 0; i < m; i++) {
        int u, v;
        fin >> u >> v;
        std::cout << "u " << i + 1 << " = " << u << "\t\tv " << i + 1 << " = " << v << "\n";
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto start = std::chrono::steady_clock::now();

    int numColors = 1; // Initial number of colors

    while (!graphColoringUtil(1)) {
        numColors++; // Increase the number of colors if a valid coloring is not found
    }

    std::cout << "\n";

    auto end = std::chrono::steady_clock::now();
    elapsedTime = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

    // Print colors
    for (int i = 1; i <= n; i++) {
        fout << "Vertex " << i << " is colored " << color[i] << std::endl;
        std::cout << "Vertex " << i << " is colored " << color[i] << std::endl;
    }

    int colorCount = getColorCount();
    std::cout << "Number of colors needed: " << colorCount << std::endl;
    fout << "Number of colors needed: " << colorCount << std::endl;

    std::cout << "Elapsed time (microseconds): " << elapsedTime << std::endl;
    fout << "Elapsed time (microseconds): " << elapsedTime << std::endl;

    return 0;
}
