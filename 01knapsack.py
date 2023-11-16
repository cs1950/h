def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    max_value = dp[n][capacity]

    # Backtrack to find the items selected in the knapsack.
    knapsack = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            
            weight, value = items[i - 1]
            knapsack.append((weight, value))
            w -= weight

    return max_value, knapsack[::-1]

# Example usage:
if __name__ == "__main__":
    n=int(input("Enter no of items: "))
    items=[list(map(int,input(f"Enter {i} Element Weight, Value:").split(" "))) for i in range(n)]
    #items = [(10, 60), (20, 100), (30, 120)]  
    capacity = int(input("Enter Knapsack Capacity: "))
    #capacity = 50

    max_value, knapsack = knapsack_01(items, capacity)

    print(f"Maximum value in the knapsack: {max_value}")
    print("Items in the knapsack:")
    for weight, value in knapsack:
        print(f"Weight: {weight}, Value: {value}, Ratio:{value/weight}")
"""Weights: {3, 4, 6, 5}

Profits: {2, 3, 1, 4}

The weight of the knapsack is 8 kg

The number of items is 4
X = {1, 1, 0, 0}
"""