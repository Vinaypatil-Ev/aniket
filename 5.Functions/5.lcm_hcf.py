def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a%b)
    
a = 14
b = 12

hc = hcf(14, 12)
print(f"HCF/GCD of {a}, {b} is {hc}")

lc = a * b / hc
print(f"LCM of {a}, {b}, is {lc}")