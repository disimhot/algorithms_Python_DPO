n, t = [int(x) for x in input().split()]
cells = [int(x) for x in input().split()]

res = "NO"
i = 1
while i < t:
    i += cells[i-1]
    if i == t:
        res = "YES"
print(res)
