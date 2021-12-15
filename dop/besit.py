import math
a, b = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

def binary_search(low, high, item):
    while low < high - 1:
        mid =  low + (high - low) // 2
        if arr[mid] == item:
            return arr[mid]
        if arr[mid] < item:
            low = mid
        else:
            high = mid
    diff_low = item - arr[low]
    diff_high = arr[high] - item
    if abs(diff_high) < abs(diff_low):
        return arr[high]
    return arr[low]
    

for i in range(len(numbers)):
    print(binary_search(0, len(numbers) - 1, numbers[i]))

