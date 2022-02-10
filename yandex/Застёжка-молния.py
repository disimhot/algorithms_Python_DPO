n = int(input())

list_1 = [int(x) for x in input().split()]
list_2 = [int(x) for x in input().split()]

for i in range(n):
    print(list_1[i], end=" ")
    print(list_2[i], end=" ")