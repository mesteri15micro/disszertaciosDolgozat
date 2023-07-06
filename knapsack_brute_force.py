import sys
import time

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"Weight = {self.weight}, with value = {self.value}"


def knapsack_brute_force(items, capacity):
    n = len(items)

    def subset_generator(n):
        for subset in range(1, 2**n):
            yield subset

    def is_subset_valid(subset):
        subset_weight = sum(items[i].weight for i in range(n) if subset & (1 << i))
        subset_value = sum(items[i].value for i in range(n) if subset & (1 << i))
        return subset_weight <= capacity, subset_value

    selected_items = []
    max_value = 0

    start_time = time.time()

    for subset in subset_generator(n):
        is_valid, subset_value = is_subset_valid(subset)

        if is_valid and subset_value > max_value:
            max_value = subset_value
            selected_items = [items[i] for i in range(n) if subset & (1 << i)]

    end_time = time.time()
    elapsed_time = int((end_time - start_time) * 1e6)

    return elapsed_time, selected_items


def read_items_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    capacity, item_line = map(int, lines[0].strip().split())
    items = []

    for line in lines[1:]:
        weight, value = map(int, line.strip().split())
        items.append(Item(weight, value))

    print("Items read from file:", capacity, len(items))

    return capacity, items


def write_output_file(items, selected_items, total_weight, total_value, elapsed_time):
    output_filename = "knapsack100_0_brute_force.out"
    with open(output_filename, 'w') as f:
        f.write("Items selected as a solution:\n")
        for item in selected_items:
            f.write("Weight = {}, with value = {}\n".format(item.weight, item.value))
        f.write("Sum weight = {}\n".format(total_weight))
        f.write("Sum value = {}\n".format(total_value))
        f.write("Elapsed time (microseconds): {}".format(elapsed_time))


def main():
    input_filename = "knapsack100_0.in"

    capacity, items = read_items_from_file(input_filename)

    if capacity <= 0:
        print("Invalid capacity value in the input file.")
        return
    if not items:
        print("No items found in the input file.")
        return

    elapsed_time, selected_items = knapsack_brute_force(items, capacity)

    total_weight = sum(item.weight for item in selected_items)
    total_value = sum(item.value for item in selected_items)

    write_output_file(items, selected_items, total_weight, total_value, elapsed_time)
    print("Program finished")


if __name__ == "__main__":
    main()
