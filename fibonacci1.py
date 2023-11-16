import time 

def rFib(n):
  if n == 0 or n == 1:
    return n
  return rFib(n - 1) + rFib(n - 2)


def Fib(n):
  n0 = 0
  n1 = 1
  i = 1
  while i != n:
    n0, n1 = n1, n0 + n1
    i += 1
  return n1

x=int(input("Enter Number: "))
start_time = time.time()
a=Fib(x)
end_time = time.time()

rstart_time = time.time()
b=rFib(x)
rend_time = time.time()

print(f"Non-Recursive Fibonacci: {a} \nTime:{(end_time-start_time):.6f} seconds\n")
print(f"Recursive Fibonacci: {b} \nTime:{(rend_time-rstart_time):.6f} seconds\n")
