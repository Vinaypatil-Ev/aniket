def mul(a, b):
    arr = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(a)):
                arr[i][j] += a[i][k] * b[k][j]
    return arr
            


if __name__ == "__main__":
    a = [
        [1, 1, 1],
        [10, 30, 10],
        [30, 20, 20],
    ]
    b = [
        [5, 6, 8],
        [9, 8, 7],
        [1, 5, 9],
    ]
    matrix = mul(a, b)
    print(matrix)