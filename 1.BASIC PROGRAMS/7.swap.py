# WAP to demonstrate arithmetic operation on two integer numbers.

# with third variable
print("Enter two no")
a = int(input("Enter first No: "))
b = int(input("Enter second No: "))
c = b
b = a
a = c
print(f"swap using third variable: {a}, {b}")

# without third varible
print("\nEnter two no")
a = int(input("Enter first No: "))
b = int(input("Enter second No: "))
a = a + b
b = a - b
a = a - b
print(f"swap without third variable: {a}, {b}")

#without third varible multiplication
print("\nEnter two no")
a = int(input("Enter first No: "))
b = int(input("Enter second No: "))
a = a * b
b = a / b
a = a / b
print(f"swap without third variable: {int(a)}, {int(b)}")