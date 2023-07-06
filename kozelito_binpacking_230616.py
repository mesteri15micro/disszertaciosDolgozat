import time

def quicksort(arr, low, high):
    stack = []
    stack.append((low, high))

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] > pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]

            partition = i + 1

            stack.append((low, partition - 1))
            stack.append((partition + 1, high))



def approximateBinPacking(items, binCapacity):
    n = len(items)
    binSizes = []

    quicksort(items, 0, n - 1)

    start = time.time()

    for i in range(n):
        currentItem = items[i]
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
        sizes = fin.readline().split()
        for size in sizes:
            items.append(float(size))

    approximateBinPacking(items, binCapacity)

if __name__ == "__main__":
    main()
