# WAP to sort array in ascending order
def find_min(arr, start, end):
    index = start
    e = arr[index]
    start += 1
    while start < end:
        if e > arr[start]:
            index = start
            e = arr[start]
        start += 1
    return index

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    
def sort_arr(arr, n):
    for i in range(n - 1):
        index = find_min(arr, i+1, n)
        if arr[i] > arr[index]:
            swap(arr, i, index)

arr = [100, 29, 1, 5, 78, 99, 102]
n = len(arr)
sort_arr(arr, n)
print(arr)