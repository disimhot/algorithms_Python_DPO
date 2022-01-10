n, m = [int(x) for x in input().split()]
k = 0
while m > n: 
    if m % 2 == 1:
        m+= 1
    else:
        m /= 2
    k+=1

print(int(abs(m - n)) + k)
