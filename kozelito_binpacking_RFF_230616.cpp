#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Quicksort subroutine to sort elements in increasing order
void quicksort(vector<float>& arr, int low, int high) {
    if (low < high) {
        float pivot = arr[high];
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) { // Modified comparison operator
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);

        int partition = i + 1;

        quicksort(arr, low, partition - 1);
        quicksort(arr, partition + 1, high);
    }
}

// Function to perform approximate bin packing
void approximateBinPacking(vector<float>& items, float binCapacity) {
    int n = items.size();
    vector<float> binSizes; // Array to store bin sizes

    // Sort the items in increasing order using quicksort
    //quicksort(items, 0, n - 1);

    // Measure the execution time of the approximate bin packing algorithm
    auto start = high_resolution_clock::now();

    // Iterate over each item
    for (int i = 0; i < n; i++) {
        float currentItem = items[i];
        bool placed = false;

        // Try to place the item in an existing bin
        for (int j = 0; j < binSizes.size(); j++) {
            if (binSizes[j] >= currentItem) {
                binSizes[j] -= currentItem;
                placed = true;
                break;
            }
        }

        // If the item couldn't be placed in an existing bin, create a new bin
        if (!placed) {
            binSizes.push_back(binCapacity - currentItem);
        }
    }

    // Print the approximate solution
    cout << "Number of bins used: " << binSizes.size() << endl;
    
    // Open the output file
    ofstream fout("binpacking10000_5.out");

    // Write the approximate solution to the output file
    fout << "Number of bins used: " << binSizes.size() << endl;
    for (int i = 0; i < binSizes.size(); i++) {
        cout << "Bin " << i + 1 << " size: " << binCapacity - binSizes[i] << endl;
        fout << "Bin " << i + 1 << " size: " << binCapacity - binSizes[i] << endl;
    }

    auto end = high_resolution_clock::now();

    // Calculate the elapsed time
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Execution time: " << duration.count() << " milliseconds" << endl;
    fout << "Execution time: " << duration.count() << " milliseconds" << endl;

    // Close the output file
    fout.close();
}

int main() {
    int n; // Number of elements
    float binCapacity; // Capacity of each bin
    vector<float> items; // Array of element sizes

    // Read input from the input file
    ifstream fin("binpacking10000_5.in");
    fin >> n;
    cout << n << "\n";
    binCapacity = 1;
    cout << binCapacity << "\n";
    for (int i = 0; i < n; i++) {
        float size;
        fin >> size;
        items.push_back(size);
    }
    fin.close();

    approximateBinPacking(items, binCapacity);

    return 0;
}
