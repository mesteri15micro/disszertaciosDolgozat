import matplotlib.pyplot as plt

# Function to perform the knapsack algorithm
def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    # Retrieve the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items

# Generate random item weights and values
items = [(5, 10), (10, 20), (15, 30), (20, 40), (25, 50), (30, 60), (35, 70), (40, 80), (45, 90), (50, 100)]

# Set knapsack capacity
capacity = 100

# Perform knapsack
max_value, selected_items = knapsack(items, capacity)

# Plotting the knapsack
fig, ax = plt.subplots()
ax.set_title('Knapsack Visualization')
ax.set_xlabel('Weight')
ax.set_ylabel('Value')

# Plot all items
for item in items:
    ax.scatter(item[0], item[1], marker='o', color='blue')

# Plot selected items
for item in selected_items:
    ax.scatter(item[0], item[1], marker='s', color='red')

# Annotate selected items
for item in selected_items:
    ax.annotate(f'({item[0]},{item[1]})', (item[0], item[1]), ha='center', va='bottom', color='red')

# Set the x-axis and y-axis limits
ax.set_xlim(0, max(item[0] for item in items) + 5)
ax.set_ylim(0, max(item[1] for item in items) + 10)

plt.show()
