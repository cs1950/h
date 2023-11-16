def fractional_knapsack(items, capacity):

    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    knapsack = []

    for weight, value in items:
        if capacity == 0:
            break

        fraction = min(1, capacity / weight)
        value_in_knapsack = fraction * value
        total_value += value_in_knapsack
        capacity -= fraction * weight
        knapsack.append((weight, fraction, value_in_knapsack))

    return total_value, knapsack


# Example usage:
if __name__ == "__main__":
    n=int(input("Enter no of items: "))
    items=[list(map(int,input(f"Enter {i} Element Weight, Value:").split(" "))) for i in range(n)]
    #items = [(10, 60), (20, 100), (30, 120)]  
    capacity = int(input("Enter Knapsack Capacity: "))
    #capacity = 50
    total_value, knapsack = fractional_knapsack(items, capacity)

    print(f"\nTotal value in the knapsack: {total_value}")
    print("Items in the knapsack:")
    for weight, fraction, value in knapsack:
        print(f"Weight: {weight}, Fraction taken: {fraction}, Value in knapsack: {value}")
"""
Item	Weight	Value
1	    5	      30
2	    10	    40
3	    15	    45
4	    22	    77
5	    25	    90

Knapsack Capacity: 60
"""
"""Item (xi)	Value (vi)	Weight (wi)	pi = vi / wi
I2	25	15	1.67
I1	24	18	1.33
I3	15	20	0.75

Knapsack capacity M = 20.
The knapsack is full. Fractional Greedy algorithm selects items { I2, I1 * 5/18 }, and it gives a profit of 31.67 units.
"""
