import random
import time

def random_select(items, num):
    random_items = []
    remaining_indices = set(range(len(items)))

    for _ in range(num):
        index = random.choice(list(remaining_indices))
        random_items.append(items[index])
        remaining_indices.remove(index)

    return random_items

def approximateBinPacking(items, binCapacity):
    n = len(items)
    binSizes = []

    randomItems = random_select(items, n)  # Randomly select unique items

    start = time.time()

    for i in range(n):
        currentItem = randomItems[i]
        placed = False

        for j in range(len(binSizes)):
            if binSizes[j] >= currentItem:
                binSizes[j] -= currentItem
                placed = True
                break

        if not placed:
            binSizes.append(binCapacity - currentItem)

    print("Number of bins used:", len(binSizes))

    with open("binpacking10000_9.out", "w") as fout:
        fout.write("Number of bins used: " + str(len(binSizes)) + "\n")
        for i in range(len(binSizes)):
            print("Bin", i + 1, "size:", binCapacity - binSizes[i])
            fout.write("Bin " + str(i + 1) + " size: " + str(binCapacity - binSizes[i]) + "\n")

    end = time.time()
    duration = end - start
    print("Execution time:", duration, "seconds")

def main():
    filename = "binpacking10000_9.in"
    items = []

    with open(filename, "r") as fin:
        n = int(fin.readline().strip())
        binCapacity = 1
        sizes = fin.readline().strip().split()  # Read all sizes as strings
        items = [float(size) for size in sizes]  # Convert sizes to float

    approximateBinPacking(items, binCapacity)

if __name__ == "__main__":
    main()
