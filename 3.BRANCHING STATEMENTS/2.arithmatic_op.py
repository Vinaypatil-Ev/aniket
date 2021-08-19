# WAP using switch case for arithmetic operation on two numbers, if user enters an operator as
# choice, the appropriate operation should perform.
# If user enters wrong choice appropriate message should get displayed.
# i.e. + is for addition
# - is for subtraction


ops = {"+", "-", "/", "*"}
print("enter 2 nos")
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
print("Arithmatic operator")
op = input("op: ")
while op not in ops:
    print("Enter correct op (+-*/)")
    op = input("op: ")
swith = {"+": a + b, "-": a - b, "*": a * b, "/": "a/b"}
print(f"{a} {op} {b} = {swith[op]}")