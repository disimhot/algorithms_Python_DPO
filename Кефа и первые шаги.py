n = int(input()) 
array = [int(x) for x in input().split()]

res = 1
tempRes = 1

for i in range(1, n):
    if array[i-1] <= array[i]:
        tempRes = tempRes + 1
    else:
        res = max(res, tempRes)
        tempRes = 1
res = max(res, tempRes)
print(res)
