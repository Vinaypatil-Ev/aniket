def gcd(a, b):
    if b == 0:
        return a
    return gcd(a, a%b)

x = gcd(gcd(10, 14), 40)
print(x)