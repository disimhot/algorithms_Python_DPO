# 1 способ рекурсивн0
# асимптотика O(fib(n))
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# решение черещ массив
# O(N-2)
n = int(input())

fib = [0, 1] + [0]*(n-1)

for i in range(2, n + 1):
    fib[i] = fib[i-2] +fib[i-1]

print(fib[n])