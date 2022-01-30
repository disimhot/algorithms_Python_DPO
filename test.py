# # сложность сортировки выбором O(n2)
def find_smallest(arr):
    i_sm = 0
    for i in range(len(arr)):
        if arr[i] < arr[i_sm]:
            i_sm = i
    return i_sm

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallestidx = find_smallest(arr)
        new_arr.append(arr.pop(smallestidx))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
print(selection_sort([0, 1000, 1]))
print(selection_sort([-1, -2, 1]))




a = [1,2,13,1121,121212]
b = [1,2,13,1121]

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == item:
            return item
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid



res = binary_search(a, 1)
print(res)
res1 = binary_search(a, 121212)
print(res1)
res2 = binary_search(a, 13)
print(res2)

print()
res3 = binary_search(b, 1)
print(res3)
res4 = binary_search(b, 1121)
print(res4)
res5 = binary_search(b, 13)
print(res5)
