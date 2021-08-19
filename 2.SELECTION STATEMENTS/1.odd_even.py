# WAP to check whether a number is even or odd

def iseven(no):
    return no % 2 == 0

no = int(input("Enter the no: "))
x = iseven(no)
if x:
    print(f"{no} is even")
else:
    print(f"{no} is odd")