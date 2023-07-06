#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

std::vector<float> random_select(const std::vector<float>& items, int num) {
    std::vector<float> random_items;
    std::vector<int> remaining_indices(items.size());
    for (int i = 0; i < items.size(); ++i) {
        remaining_indices[i] = i;
    }

    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::shuffle(remaining_indices.begin(), remaining_indices.end(), std::default_random_engine(seed));

    for (int i = 0; i < num; ++i) {
        int index = remaining_indices[i];
        random_items.push_back(items[index]);
    }

    return random_items;
}

void approximateBinPacking(const std::vector<float>& items, float binCapacity) {
    int n = items.size();
    std::vector<float> binSizes;

    std::vector<float> randomItems = random_select(items, n); // Randomly select unique items

    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < n; ++i) {
        float currentItem = randomItems[i];
        bool placed = false;

        for (size_t j = 0; j < binSizes.size(); ++j) {
            if (binSizes[j] >= currentItem) {
                binSizes[j] -= currentItem;
                placed = true;
                break;
            }
        }

        if (!placed) {
            binSizes.push_back(binCapacity - currentItem);
        }
    }

    std::cout << "Number of bins used: " << binSizes.size() << std::endl;

    std::ofstream fout("binpacking10000_9.out");
    fout << "Number of bins used: " << binSizes.size() << std::endl;
    for (size_t i = 0; i < binSizes.size(); ++i) {
        std::cout << "Bin " << i + 1 << " size: " << binCapacity - binSizes[i] << std::endl;
        fout << "Bin " << i + 1 << " size: " << binCapacity - binSizes[i] << std::endl;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Execution time: " << duration.count() << " seconds" << std::endl;
    fout << "Execution time: " << duration.count() << " seconds" << std::endl;
}

int main() {
    std::string filename = "binpacking10000_9.in";
    std::vector<float> items;

    std::ifstream fin(filename);
    int n;
    fin >> n;
    float binCapacity = 1.0f;

    items.resize(n);
    for (int i = 0; i < n; ++i) {
        fin >> items[i];
    }

    approximateBinPacking(items, binCapacity);

    return 0;
}
