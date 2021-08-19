def fib(n, arr):
    if arr[n - 1] is None:
        arr[n - 1] = fib(n - 1, arr) + fib(n - 2, arr)
    return arr[n - 1]

no = 7
arr = [None] * no
arr[0] = 1
arr[1] = 1
fib(7, arr)
print(f"fibo of first {no}: ")
print(arr)
