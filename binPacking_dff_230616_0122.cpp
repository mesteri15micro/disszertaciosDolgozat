#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <chrono>

using namespace std;
using namespace std::chrono;

ifstream fin("binpacking10.in");
ofstream fout("binpacking10.out");

// Quicksort subroutine to sort elements in descending order
void quicksort(vector<double>& arr, int left, int right) {
    if (left >= right) {
        return;
    }

    double pivot = arr[(left + right) / 2];
    int i = left, j = right;

    while (i <= j) {
        while (arr[i] > pivot) {
            i++;
        }
        while (arr[j] < pivot) {
            j--;
        }
        if (i <= j) {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    quicksort(arr, left, j);
    quicksort(arr, i, right);
}

// Bin packing algorithm
void binPacking(vector<double>& s) {
    int n = s.size();

    // Step 2: Initialize Bj sets and bj values
    vector<vector<int>> Bj(n);
    vector<double> bj(n, 0);

    // Step 3: Iterate over elements in s
    for (int t = 0; t < n; t++) {
        // Step 4: Initialize j
        int j = 0;

        // Step 5: Find the smallest bin j such that bj + sit <= 1
        while (j < n && bj[j] + s[t] > 1) {
            j++;
        }

        // Step 6: Add t to Bj[j] and update bj[j]
        Bj[j].push_back(t);
        bj[j] += s[t];
    }

    // Output the bins
    for (int j = 0; j < n; j++) {
        if (Bj[j].empty()) {
            break;
        }

        cout << "Bin " << j + 1 << ": ";
        for (auto t : Bj[j]) {
            cout << s[t] << " ";
            fout << s[t] << " ";
        }
        cout << endl;
        fout << endl;
    }
}

int main() {
    int n;
    //cin >> n;
    fin >> n;
    cout << n << "\n";

    vector<double> s(n);
    /*for (int i = 0; i < n; i++) {
        cin >> s[i];
    }*/
    for (int i = 0; i < n; i++) {
        fin >> s[i];
        cout << s[i] << "\t";
    }
    cout << "\n";

    // Sort elements in descending order using Quicksort
    quicksort(s, 0, n - 1);

    // Measure the execution time of bin packing algorithm
    auto start = high_resolution_clock::now();
    binPacking(s);
    auto end = high_resolution_clock::now();

    // Calculate the elapsed time
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Execution time: " << duration.count() << " milliseconds" << endl;
    fout << "Execution time: " << duration.count() << " milliseconds" << endl;

    return 0;
}
