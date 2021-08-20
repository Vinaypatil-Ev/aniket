# WAP to find greatest and smallest number in an array.

def find_max_and_small(arr, n):
    greater = arr[0]
    smaller = arr[0]
    for i in range(1, n):
        if arr[i] > greater:
            greater = arr[i]
        if arr[i] < smaller:
            smaller = arr[i]
    return greater, smaller
        



if __name__ == "__main__":
    arr = [5, 90, 46, 29, 99, 100, 7, 1, 12, 2]
    n = len(arr)
    m, s = find_max_and_small(arr, n)
    print(f"Max: {m}, Min: {s}")