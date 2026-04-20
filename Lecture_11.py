def sigma(n):
    # """Returns the sum of the first n natural numbers."""
    if n == 1:
        return n
    else:
        # print(n)
        return n + sigma(n - 1)

n = 10
print(n, sigma(n))

def factorial(n):
    # """Returns the factorial of n."""
    if n == 1:
        return n
    else:
        # print(n)
        return n * factorial(n - 1)
n = 3
print(n, factorial(n))

def fibonacci(n):   
    # """Returns the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for n in range(10):
    print(n, fibonacci(n))

counter = 0
def fibo(n):
    # """Returns the nth Fibonacci number with a counter to track calls."""
    global counter
    counter += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    

n = int(input("Enter n: "))
import time
start_time = time.time()
fibo(n)
print("Counter", counter)
print(time.time() - start_time)

def fibo_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

n = int(input("Enter n: "))
import time
start_time = time.time()
fibo_iterative(n)
print(time.time() - start_time)

# Memoization
memo = {0: 0, 1: 1}
counter = 0
def fibo_memo(n):
    # """Returns the nth Fibonacci number using memoization."""
    global counter
    counter += 1
    if n not in memo:
        memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
        print(n, memo[n])
    return memo[n]

n = int(input("Enter n: "))
import time
start_time = time.time()
fibo_memo(n)
print("Counter", counter)
print(time.time() - start_time)
print(memo)

# Hanoi Towers
def hanoi(n, start, mid, end):
    # """Solves the Tower of Hanoi problem."""
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
    else:
        # n-1개의 원판을 start에서 mid로 이동
        hanoi(n - 1, start, end, mid)
        # 가장 큰 원판을 start에서 end로 이동
        print(f"Move disk {n} from {start} to {end}")
        # n-1개의 원판을 mid에서 end로 이동
        hanoi(n - 1, mid, start, end)
n=3
hanoi(n, 'A', 'B', 'C')