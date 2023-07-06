//hatizsak_kozelito_RFF

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

int partition(vector<Item>& arr, int low, int high) {
    int pivot = arr[high].value;
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j].value > pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quicksort(vector<Item>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

vector<Item> knapsackApproximation(vector<Item>& items, int capacity, double& elapsedTime) {
    auto start = chrono::steady_clock::now();

    //quicksort(items, 0, items.size() - 1);

    vector<Item> selectedItems;
    int currentWeight = 0;
    int totalValue = 0;

    for (const Item& item : items) {
        if (currentWeight + item.weight <= capacity) {
            selectedItems.push_back(item);
            currentWeight += item.weight;
            totalValue += item.value;
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

int main() {
    int capacity;
    vector<Item> items = readItemsFromFile("knapsack100_9.in", capacity);

    double elapsedTime;
    vector<Item> selectedItems = knapsackApproximation(items, capacity, elapsedTime);

    ofstream outputFile("knapsack100_9.out");
    if (outputFile.is_open()) {
        outputFile << "Item selected as a solution:" << endl;
        for (const Item& item : selectedItems) {
            outputFile << "Weight = " << item.weight << ", with value = " << item.value << endl;
        }

        int currentWeight = 0;
        int totalValue = 0;
        for (const Item& item : selectedItems) {
            currentWeight += item.weight;
            totalValue += item.value;
        }

        outputFile << "Sum weight = " << currentWeight << endl;
        outputFile << "Sum value = " << totalValue << endl;
        outputFile << "Elapsed time (microseconds): " << elapsedTime << endl;

        outputFile.close();
        cout << "Output saved to 'knapsack100_9.out'." << endl;
    }
    else {
        cerr << "Unable to open the output file." << endl;
    }

    return 0;
}
