# WAP to calculate factorial of a number using a function

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
n = 5
x = fact(n)
print(f"factorial of {n} is {x}")