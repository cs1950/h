import time
import sys

def rFib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_series = rFib(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

def Fib(n):
    n0, n1 = 0, 1
    series = [n0, n1]
    for i in range(2, n):
        n0, n1 = n1, n0 + n1
        series.append(n1)
    return series

def get_space_complexity(obj):
    return sys.getsizeof(obj)

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

x = int(input("Enter Number: "))

# Non-Recursive Fibonacci
a, time_a = measure_time(Fib, x)
space_a = get_space_complexity(a)
print(f"Non-Recursive Fibonacci Series: {a} \nTime: {time_a:.6f} seconds\nSpace: {space_a} bytes\n")

# Recursive Fibonacci
b, time_b = measure_time(rFib, x-1)
space_b = get_space_complexity(b)
print(f"Recursive Fibonacci Series: {b} \nTime: {time_b:.6f} seconds\nSpace: {space_b} bytes\n")
