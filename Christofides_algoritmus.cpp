#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Point {
    int x, y;
};

double calculateDistance(const Point& p1, const Point& p2) {
    int dx = p1.x - p2.x;
    int dy = p1.y - p2.y;
    return sqrt(dx * dx + dy * dy);
}

struct Graph {
    int V;
    vector<Point> points;
    vector<vector<double>> distances;

    Graph(int vertices) : V(vertices), distances(vertices, vector<double>(vertices, 0.0)) {}

    void addPoint(const Point& p) {
        points.push_back(p);
    }

    void calculateDistances() {
        for (int i = 0; i < V; i++) {
            for (int j = i + 1; j < V; j++) {
                double distance = calculateDistance(points[i], points[j]);
                distances[i][j] = distance;
                distances[j][i] = distance;
            }
        }
    }
};

void printTour(const vector<int>& tour) {
    cout << "Tour: ";
    for (int i : tour) {
        cout << i << " ";
    }
    cout << endl;
}

double calculateTourLength(const vector<int>& tour, const Graph& graph) {
    double length = 0.0;
    int n = graph.V;
    for (int i = 0; i < n; i++) {
        int u = tour[i];
        int v = tour[(i + 1) % n];
        length += graph.distances[u][v];
    }
    return length;
}

void findMinimumMatching(const Graph& graph, vector<vector<double>>& weightMatrix, vector<int>& matching) {
    int n = graph.V;
    vector<bool> visited(n, false);

    // Find minimum-weight matching for each vertex
    for (int u = 0; u < n; u++) {
        if (visited[u])
            continue;
        double minWeight = INF;
        int minVertex = -1;
        for (int v = 0; v < n; v++) {
            if (u == v || visited[v])
                continue;
            if (weightMatrix[u][v] < minWeight) {
                minWeight = weightMatrix[u][v];
                minVertex = v;
            }
        }
        matching[u] = minVertex;
        matching[minVertex] = u;
        visited[u] = true;
        visited[minVertex] = true;
    }
}

void findEulerianTour(int v, const Graph& graph, vector<vector<double>>& weightMatrix, vector<int>& tour) {
    int n = graph.V;
    for (int u = 0; u < n; u++) {
        if (weightMatrix[v][u] > 0) {
            weightMatrix[v][u] = 0;
            weightMatrix[u][v] = 0;
            findEulerianTour(u, graph, weightMatrix, tour);
        }
    }
    tour.push_back(v);
}

vector<int> findHamiltonianTour(const Graph& graph, const vector<int>& matching, const vector<int>& eulerianTour) {
    int n = graph.V;
    vector<bool> visited(n, false);
    vector<int> tour;
    for (int v : eulerianTour) {
        if (!visited[v]) {
            tour.push_back(v);
            visited[v] = true;
        }
    }
    for (int v : matching) {
        if (!visited[v]) {
            tour.push_back(v);
            visited[v] = true;
        }
    }
    return tour;
}

vector<int> christofides(const Graph& graph) {
    int n = graph.V;

    // Step 1: Calculate minimum spanning tree
    vector<vector<double>> weightMatrix = graph.distances;
    vector<int> parent(n, -1);
    vector<double> key(n, INF);
    vector<bool> inMST(n, false);

    key[0] = 0;
    for (int count = 0; count < n - 1; count++) {
        double minWeight = INF;
        int minVertex = -1;

        for (int v = 0; v < n; v++) {
            if (!inMST[v] && key[v] < minWeight) {
                minWeight = key[v];
                minVertex = v;
            }
        }

        inMST[minVertex] = true;

        for (int v = 0; v < n; v++) {
            if (weightMatrix[minVertex][v] > 0 && !inMST[v] && weightMatrix[minVertex][v] < key[v]) {
                parent[v] = minVertex;
                key[v] = weightMatrix[minVertex][v];
            }
        }
    }

    // Step 2: Create a set of vertices with odd degree in the MST
    vector<int> oddVertices;
    for (int v = 0; v < n; v++) {
        if (graph.adjacencyList[v].size() % 2 == 1) {
            oddVertices.push_back(v);
        }
    }

    // Step 3: Find minimum-weight perfect matching on the induced subgraph
    vector<int> matching(n, -1);
    findMinimumMatching(graph, weightMatrix, matching);

    // Step 4: Construct a multigraph combining the MST and the matching
    vector<int> eulerianTour;
    for (int v : oddVertices) {
        eulerianTour.push_back(v);
    }
    findEulerianTour(0, graph, weightMatrix, eulerianTour);

    // Step 5: Find Hamiltonian tour by skipping repeated vertices
    vector<int> tour = findHamiltonianTour(graph, matching, eulerianTour);

    return tour;
}

int main() {
    ifstream fin("tsp.in");
    ofstream fout("tsp.out");

    // Read input
    int n; // Number of vertices
    fin >> n;

    Graph graph(n);
    for (int i = 0; i < n; i++) {
        Point p;
        fin >> p.x >> p.y;
        graph.addPoint(p);
    }

    // Calculate distances between points
    graph.calculateDistances();

    auto start = chrono::steady_clock::now();

    // Solve TSP using Christofides algorithm
    vector<int> tour = christofides(graph);

    auto end = chrono::steady_clock::now();
    double elapsedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    // Print tour and tour length
    printTour(tour);
    double tourLength = calculateTourLength(tour, graph);
    cout << "Tour length: " << tourLength << endl;
    cout << "Elapsed time (microseconds): " << elapsedTime << endl;

    return 0;
}


