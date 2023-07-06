#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <unordered_set>
#include <chrono>

using namespace std;

const int MAXN = 10100; // Maximum number of vertices

int n; // Number of vertices
vector<int> adj[MAXN]; // Adjacency list of the graph
int color[MAXN]; // Array of vertex colors

int getColorCount() {
    unordered_set<int> colorSet;
    for (int i = 1; i <= n; i++) {
        colorSet.insert(color[i]);
    }
    return colorSet.size();
}

void quicksort(vector<int>& vertices, int low, int high) {
    if (low < high) {
        int pivot = vertices[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (vertices[j] > pivot) {
                i++;
                swap(vertices[i], vertices[j]);
            }
        }

        swap(vertices[i + 1], vertices[high]);

        int pivotIndex = i + 1;

        quicksort(vertices, low, pivotIndex - 1);
        quicksort(vertices, pivotIndex + 1, high);
    }
}

int main() {
    ifstream fin("graphcoloring10.in");
    ofstream fout("graphcoloring10.out");

    double elapsedTime;
    // Read input
    int m; // Number of edges
    fin >> n >> m;
    cout << "n=" << n << "\t\tm=" << m << "\n";
    for (int i = 0; i < m; i++) {
        int u, v;
        fin >> u >> v;
        cout << "u " << i + 1 << " = " << u << "\t\tv " << i + 1 << " = " << v << "\n";
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> vertices;
    for (int i = 1; i <= n; i++) {
        vertices.push_back(i);
    }

    auto start = chrono::steady_clock::now();

    // Sort vertices in descending order
    quicksort(vertices, 0, n - 1);

    // Color vertices
    for (int i = 0; i < n; i++) {
        int vertex = vertices[i];
        int c = 1;
        for (int j = 0; j < adj[vertex].size(); j++) {
            int v = adj[vertex][j];
            if (color[v] == c) {
                c++;
                j = -1; // restart the loop
            }
        }
        color[vertex] = c;
    }

    auto end = chrono::steady_clock::now();
    elapsedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    // Print colors
    for (int i = 1; i <= n; i++) {
        fout << "Vertex " << i << " is colored " << color[i] << endl;
        cout << "Vertex " << i << " is colored " << color[i] << endl;
    }

    int colorCount = getColorCount();
    cout << "Number of colors needed: " << colorCount << endl;
    fout << "Number of colors needed: " << colorCount << endl;

    cout << "Elapsed time (microseconds): " << elapsedTime << endl;
    fout << "Elapsed time (microseconds): " << elapsedTime << endl;

    return 0;
}
