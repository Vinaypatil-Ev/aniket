# WAP to check whether Number is positive or negative or ZERO.


no = int(input("Enter the no: "))
if no == 0:
    print(f"It is 0")
elif no < 0:
    print(f"{no} is Negative")
else:
    print(f"{no} is positive")