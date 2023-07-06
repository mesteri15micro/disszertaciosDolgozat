//dinamikus programozassal megoldva

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;

struct Item {
    int weight;
    int value;
};

vector<Item> knapsack100_9Approximation(vector<Item>& items, int capacity, double& elapsedTime) {
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    auto start = chrono::steady_clock::now();

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= capacity; j++) {
            if (items[i - 1].weight <= j) {
                dp[i][j] = max(dp[i - 1][j], items[i - 1].value + dp[i - 1][j - items[i - 1].weight]);
            }
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    vector<Item> selectedItems;
    int i = n, j = capacity;
    while (i > 0 && j > 0) {
        if (dp[i][j] != dp[i - 1][j]) {
            selectedItems.push_back(items[i - 1]);
            j -= items[i - 1].weight;
        }
        i--;
    }

    reverse(selectedItems.begin(), selectedItems.end());

    auto end = chrono::steady_clock::now();
    elapsedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    return selectedItems;
}

vector<Item> readItemsFromFile(const string& filename, int& capacity) {
    ifstream inputFile(filename);
    vector<Item> items;

    if (inputFile.is_open()) {
        inputFile >> capacity;
        int weight, value;
        while (inputFile >> weight >> value) {
            items.push_back({ weight, value });
        }

        inputFile.close();
    }
    else {
        cerr << "Unable to open the input file." << endl;
    }

    return items;
}

void writeOutputToFile(const string& filename, const vector<Item>& selectedItems, int totalWeight, int totalValue, double elapsedTime) {
    ofstream outputFile(filename);

    if (outputFile.is_open()) {
        outputFile << "Items selected as a solution:" << endl;
        for (const Item& item : selectedItems) {
            outputFile << "Weight = " << item.weight << ", with value = " << item.value << endl;
        }

        outputFile << "Sum weight = " << totalWeight << endl;
        outputFile << "Sum value = " << totalValue << endl;
        outputFile << "Elapsed time (microseconds): " << elapsedTime << endl;

        outputFile.close();
    }
    else {
        cerr << "Unable to open the output file." << endl;
    }
}

int main() {
    int capacity;
    vector<Item> items = readItemsFromFile("knapsack100_9.in", capacity);

    if (capacity <= 0) {
        cerr << "Invalid capacity value in the input file." << endl;
        return 1;
    }

    if (items.empty()) {
        cerr << "No items found in the input file." << endl;
        return 1;
    }

    double elapsedTime;

    vector<Item> selectedItems = knapsack100_9Approximation(items, capacity, elapsedTime);

    int totalWeight = 0;
    int totalValue = 0;
    for (const Item& item : selectedItems) {
        totalWeight += item.weight;
        totalValue += item.value;
    }

    writeOutputToFile("knapsack100_9.out", selectedItems, totalWeight, totalValue, elapsedTime);

    return 0;
}
