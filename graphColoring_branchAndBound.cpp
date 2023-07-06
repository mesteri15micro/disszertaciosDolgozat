
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <chrono>
#include <climits>

using namespace std;

const int MAXN = 1000; // Maximum number of vertices

int n; // Number of vertices
vector<int> adj[MAXN]; // Adjacency list of the graph
int color[MAXN]; // Array of vertex colors
int minColors; // Minimum number of colors found so far

bool isSafe(int v, int c) {
    for (int u : adj[v]) {
        if (color[u] == c) {
            return false;
        }
    }
    return true;
}

void graphColoringUtil(int v, int colorsUsed) {
    if (v == n) {
        minColors = min(minColors, colorsUsed);
        return;
    }

    for (int c = 1; c <= colorsUsed + 1; c++) {
        if (isSafe(v, c)) {
            color[v] = c;
            graphColoringUtil(v + 1, colorsUsed);
            color[v] = 0;
        }
    }
}

int graphColoring() {
    minColors = INT_MAX;
    graphColoringUtil(0, 0);
    return minColors;
}

int main() {
    ifstream fin("graphcoloring.in");
    ofstream fout("graphcoloring.out");

    // Read input
    int m; // Number of edges
    fin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v;
        fin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto start = chrono::steady_clock::now();

    int numColors = graphColoring();

    auto end = chrono::steady_clock::now();
    double elapsedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    // Print colors
    for (int i = 0; i < n; i++) {
        fout << "Vertex " << i + 1 << " is colored " << color[i] << endl;
        cout << "Vertex " << i + 1 << " is colored " << color[i] << endl;
    }

    fout << "Number of colors needed: " << numColors << endl;
    cout << "Number of colors needed: " << numColors << endl;

    fout << "Elapsed time (microseconds): " << elapsedTime << endl;
    cout << "Elapsed time (microseconds): " << elapsedTime << endl;

    return 0;
}



