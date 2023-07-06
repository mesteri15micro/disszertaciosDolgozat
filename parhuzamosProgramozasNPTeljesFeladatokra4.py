import multiprocessing
import networkx as nx

def binPacking(items, binCapacity):
    bins = []
    items.sort(reverse=True)
    for item in items:
        added = False
        for bin in bins:
            if bin['capacity'] >= item:
                bin['items'].append(item)
                bin['capacity'] -= item
                added = True
                break
        if not added:
            newBin = {'capacity': binCapacity, 'items': [item]}
            bins.append(newBin)
    return bins

def binPackingParallel(items, binCapacity):
    num_processors = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_processors)
    chunk_size = max(len(items) // num_processors, 1)
    results = pool.starmap(binPacking, [(items[i:i+chunk_size], binCapacity) for i in range(0, len(items), chunk_size)])
    pool.close()
    pool.join()
    bins = [bin for sublist in results for bin in sublist]
    return bins

def knapsack(items, capacity):
    num_items = len(items)
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = num_items, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1][0]
        i -= 1

    return dp[num_items][capacity], selected_items[::-1]

def knapsackParallel(items, capacity):
    num_processors = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_processors)
    chunk_size = max(len(items) // num_processors, 1)
    results = pool.starmap(knapsack, [(items[i:i+chunk_size], capacity) for i in range(0, len(items), chunk_size)])
    pool.close()
    pool.join()
    max_value = max(result[0] for result in results)
    selected_items = [item for sublist in [result[1] for result in results] for item in sublist]
    return max_value, selected_items

def graphColoring(graph):
    coloring = nx.greedy_color(graph, strategy='largest_first')
    return coloring

def graphColoringParallel(graph):
    num_processors = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_processors)
    results = pool.map(graphColoring, [graph] * num_processors)
    pool.close()
    pool.join()
    coloring = max(results, key=lambda x: len(x))
    return coloring

def hamiltonianCycle(graph):
    hamiltonian_cycle = nx.algorithms.approximation.traveling_salesman_problem(graph, weight='weight')
    return hamiltonian_cycle

def hamiltonianCycleParallel(graph):
    num_processors = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_processors)
    results = pool.map(hamiltonianCycle, [graph] * num_processors)
    pool.close()
    pool.join()
    hamiltonian_cycle = min(results, key=len)
    return hamiltonian_cycle

if __name__ == '__main__':
    # Example usage
    items = [4, 8, 1, 2, 7, 5]
    binCapacity = 10
    print("Bin Packing:")
    bins = binPackingParallel(items, binCapacity)
    for i, bin in enumerate(bins):
        print(f"Bin {i+1}: {bin['items']}")
    print()
    
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 8
    print("Knapsack:")
    max_value, selected_items = knapsackParallel(items, capacity)
    print("Max Value:", max_value)
    print("Selected Items:", selected_items)
    print()
    
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
    print("Graph Coloring:")
    coloring = graphColoringParallel(graph)
    print("Coloring:", coloring)
    print()
    
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    print("Hamiltonian Cycle:")
    hamiltonian_cycle = hamiltonianCycleParallel(graph)
    print("Hamiltonian Cycle:", hamiltonian_cycle)
