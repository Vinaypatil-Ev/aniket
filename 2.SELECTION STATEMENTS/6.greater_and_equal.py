# Accept  three numbers from user and find  out largest number among three and also find out whether that three numbers are equal or not

print("Enter the three no")
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

if a >= b and a >= c:
    print(f"{a} largest amoung them")
elif b >= a and b >= c:
    print(f"{b} is largest amoung them")
else:
    print(f"{c} is largest amoung them")

if a == b == c:
    print("The are equal")