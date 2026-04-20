
a, b = 3, 9

# GCD 썡구현
# while b != 0:
#     temp = a 
#     a = b
#     b = temp % b

# GCD 반복문 구현 
def GCD(a, b):
    while(b):
        a, b = b, a%b
    return a

# GCD 재귀 구현
def gcd(a, b):
    if b:
        return a
    else:
        return gcd(a, a%b)

print(GCD(a, b), gcd(a,b))


# 소수 (에라토스테네스의 체) 판별하기
n = 199
isPrime = [True]*(n+1)

isPrime[0] = False
isPrime[1] = False

for i in range(2, int(n**0.5)+1):
    if(isPrime[i]):
        for j in range(2*i, n+1, i):
            isPrime[j] = False

for i in range(1, n):
    if(isPrime[i]):
        print(i, end=" ")
print()


# 피보나치 수열
def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1

    return fibo(n-1) + fibo(n-2)

# memoFibo
memo = {0:0, 1:1}
def memoFibo(n):
    if n not in memo:
        memo[n] = memoFibo(n-1) + memoFibo(n-2)
    return memo[n]

n = int(input())

print(fibo(n), memoFibo(n))

# 람다 식 튜플[1] 기준으로 sort
a = [(123,1233), (123,39393), (22,33313)]
print(a.sort(key = lambda x : x[1]))

# List Comprehension
arr = [i for i in range(15, 0, -2)]

# 버블 솔트
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if(arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)