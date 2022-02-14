n, a, b, c = [int(x) for x in input().split()]

K = [0]*(n+1)
allowed = [None]*(n+1)
K[0] = 0
allowed[0] = True


for i in range(1, n+1):
    K[i] = 0
    allowed[i] = False
    if i >= a and allowed[i-a] == True:
        K[i] = max(K[i], 1 + K[i-a])
        allowed[i] = True

    if i >= b and allowed[i-b] == True:
        K[i] = max(K[i], 1 + K[i-b])
        allowed[i] = True

    if i >= c and allowed[i-c] == True:
        K[i] = max(K[i], 1 + K[i-c])
        allowed[i] = True


print(K[-1])
