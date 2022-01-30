n = int(input()) 
array = [int(input())]
 
for i in range(n - 1):
    pov = int(input())
    # [1, 2] + [3, 4] = [1,2,3,4]
    array = [el + pov for el in array] + [el - pov for el in array]
    print(array)
    
 
array = [x % 360 for x in array]
if 0 in array:
    print("YES")
else:
    print("NO")