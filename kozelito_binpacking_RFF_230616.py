import time
from typing import List

# Quicksort subroutine to sort elements in increasing order
def quicksort(arr: List[float], low: int, high: int):
    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        partition = i + 1

        quicksort(arr, low, partition - 1)
        quicksort(arr, partition + 1, high)

# Function to perform approximate bin packing
def approximateBinPacking(items: List[float], binCapacity: float):
    n = len(items)
    binSizes = []  # List to store bin sizes

    # Sort the items in increasing order using quicksort
    # quicksort(items, 0, n - 1)

    # Measure the execution time of the approximate bin packing algorithm
    start = time.perf_counter()

    # Iterate over each item
    for currentItem in items:
        placed = False

        # Try to place the item in an existing bin
        for j in range(len(binSizes)):
            if binSizes[j] >= currentItem:
                binSizes[j] -= currentItem
                placed = True
                break

        # If the item couldn't be placed in an existing bin, create a new bin
        if not placed:
            binSizes.append(binCapacity - currentItem)

    # Print the approximate solution
    print("Number of bins used:", len(binSizes))

    # Open the output file
    with open("binpacking10000_9.out", "w") as fout:
        # Write the approximate solution to the output file
        fout.write("Number of bins used: " + str(len(binSizes)) + "\n")
        for i in range(len(binSizes)):
            print("Bin", i + 1, "size:", binCapacity - binSizes[i])
            fout.write("Bin " + str(i + 1) + " size: " + str(binCapacity - binSizes[i]) + "\n")

        end = time.perf_counter()

        # Calculate the elapsed time
        duration = (end - start) * 1000
        print("Execution time:", duration, "milliseconds")
        fout.write("Execution time: " + str(duration) + " milliseconds\n")

# Main function
def main():
    items = []  # List of element sizes

    # Read input from the input file
    with open("binpacking10000_9.in", "r") as fin:
        n = int(fin.readline().strip())
        print(n)
        binCapacity = 1
        print(binCapacity)
        sizes = fin.readline().strip().split()
        items = [float(size) for size in sizes]

    approximateBinPacking(items, binCapacity)

if __name__ == "__main__":
    main()
