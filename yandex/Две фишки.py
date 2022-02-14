n = int(input())
numbers = [int(x) for x in input().split()]
g = int(input())

def sum(n, numbers, guess):
    for i in range(n):
        for j in range(i + 1, n):
            if (numbers[i] + numbers[j]) == guess:
                return numbers[i], numbers[j]
    return [None]

print(*sum(n, numbers, g))