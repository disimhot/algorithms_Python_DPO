n = int(input()) 
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]

for i in range(1, n):
    row1[i] = max(row1[i-1], row1[i] + row2[i-1])
    row2[i] = max(row2[i-1], row2[i] + row1[i-1])

print(max(row1[n-1], row2[n-1]))