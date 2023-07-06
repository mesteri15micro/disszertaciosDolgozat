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

vector<Item> knapsackBruteForce(vector<Item>& items, int capacity, double& elapsedTime) {
    int n = items.size();

    auto start = chrono::steady_clock::now();

    vector<Item> selectedItems;
    int maxSum = 0;

    for (int subset = 0; subset < (1 << n); subset++) {
        int sum = 0;
        vector<Item> currentSet;
        for (int i = 0; i < n; i++) {
            if ((subset & (1 << i)) != 0) {
                sum += items[i].weight;
                currentSet.push_back(items[i]);
            }
        }
        if (sum <= capacity && sum > maxSum) {
            maxSum = sum;
            selectedItems = currentSet;
        }
    }

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

    vector<Item> selectedItems = knapsackBruteForce(items, capacity, elapsedTime);

    int totalWeight = 0;
    int totalValue = 0;
    for (const Item& item : selectedItems) {
        totalWeight += item.weight;
        totalValue += item.value;
    }

    writeOutputToFile("knapsack100_9_brute_force.out", selectedItems, totalWeight, totalValue, elapsedTime);

    return 0;
}


