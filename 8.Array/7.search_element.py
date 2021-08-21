def search(arr, ele, start, end):
    while start < end:
        if arr[start] == ele:
            return ele, start
        if arr[end] == ele:
            return ele, end
        start += 1
        end -= 1
    return 0, -1
            

if __name__ == "__main__":
    arr = [1, 2, 19, 3, 67, 5, 9, 908, 4]
    n = len(arr)
    ele, ind = search(arr, 5, 0, n - 1)
    if ele:
        print(f"{ele} is present at {ind}")
    else:
        print("not found")