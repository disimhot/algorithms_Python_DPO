n, a, b, c = [int(x) for x in input().split()]

res = 1


for i in range(0, n + 1):
    z = n - (a * i)
    if z < 0:
        continue

    for j in range(0, n + 1):
        # остаток от деления
        z = z - (b * j)
        if z >= 0:
            test = z % c
            if test == 0:
                res = max(res, i + j + (z//c))

print(res)
        
