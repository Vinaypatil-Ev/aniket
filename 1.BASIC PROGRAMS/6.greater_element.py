# WAP to demonstrate arithmetic operation on two integer numbers.

print("Enter the No")
a = int(input("Enter first NO: "))  # int() is used for type conversion
b = int(input("Enter first NO: "))
c = int(input("Enter first NO: "))

if a > b:
    if a > c:
        print(f"{a} is greter amoung them")
    else:
        print(f"{c} is greater amoung them")
else:
    print(f"{b} is greater amoung them")