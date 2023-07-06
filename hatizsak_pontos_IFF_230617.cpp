//knapsack IFF 

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;

ifstream fin("knapsack10.in");
ofstream fout("knapsack10.out");

struct Item {
    int weight;
    int value;
};

int partition(vector<Item>& items, int low, int high) {
    int pivot = items[high].value;
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (items[j].value <= pivot) {
            i++;
            swap(items[i], items[j]);
        }
    }

    swap(items[i + 1], items[high]);
    return i + 1;
}

void quicksort(vector<Item>& items, int low, int high) {
    if (low < high) {
        int pi = partition(items, low, high);

        quicksort(items, low, pi - 1);
        quicksort(items, pi + 1, high);
    }
}

vector<Item> knapsackDP(vector<Item>& items, int capacity, double& elapsedTime) {
    auto start = chrono::steady_clock::now();
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= capacity; j++) {
            if (items[i - 1].weight > j) {
                dp[i][j] = dp[i - 1][j];
            }
            else {
                dp[i][j] = max(items[i - 1].value + dp[i - 1][j - items[i - 1].weight], dp[i - 1][j]);
            }
        }
    }

    // Find the selected items
    int totalWeight = 0;
    int totalValue = 0;
    int i = n, j = capacity;
    vector<Item> selectedItems;

    while (i > 0 && j > 0) {
        if (dp[i][j] != dp[i - 1][j]) {
            selectedItems.push_back(items[i - 1]);
            totalWeight += items[i - 1].weight;
            totalValue += items[i - 1].value;
            j -= items[i - 1].weight;
        }
        i--;
    }

    cout << "Item selected as a solution:" << endl;
    fout << "Item selected as a solution:" << endl;
    for (i = selectedItems.size() - 1; i >= 0; i--) {
        cout << "Weight = " << selectedItems[i].weight << ", with value = " << selectedItems[i].value << endl;
        fout << "Weight = " << selectedItems[i].weight << ", with value = " << selectedItems[i].value << endl;
    }

    auto end = chrono::steady_clock::now();
    elapsedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    cout << "Sum weight = " << totalWeight << endl;
    fout << "Sum weight = " << totalWeight << endl;
    cout << "Sum value = " << totalValue << endl;
    fout << "Sum value = " << totalValue << endl;

    return selectedItems;
}

void sortAndKnapsack(vector<Item>& items, int capacity) {
    double elapsedTime = 0;

    quicksort(items, 0, items.size() - 1);
    vector<Item> selectedItems = knapsackDP(items, capacity, elapsedTime);

    cout << "Elapsed time (microseconds): " << elapsedTime << endl;
    fout << "Elapsed time (microseconds): " << elapsedTime << endl;
}

int main() {
    int n, capacity;
    fin >> n;
    cout << n << "\n";
    fin >> capacity;
    cout << capacity << "\n";

    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        fin >> items[i].weight >> items[i].value;
        cout << items[i].weight << "\t" << items[i].value << "\n";
        fout << items[i].weight << "\t" << items[i].value << "\n";
    }

    sortAndKnapsack(items, capacity);

    return 0;
}
