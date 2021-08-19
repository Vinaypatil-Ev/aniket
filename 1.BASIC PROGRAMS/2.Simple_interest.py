# WAP to calculate Simple interest.

def simple_intrest(p, r, t):
    si = p * r * t / 100
    return si


p = float(input("Enter principle amount: "))  # float() is used for float conversion
r = float(input("Enter the rate: "))          # input() is used for to take input
t = float(input("Enter time period: "))

x = simple_intrest(p, r, t)
print(f"Your simple intrest in {x}")