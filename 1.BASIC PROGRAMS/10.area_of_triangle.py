# Command line program to find area of triangle
def area(b, h):
    return b * h / 2

b = float(input("Enter the base of triangle: "))
h = float(input("Enter the height of triangle: "))

x = area(b, h)

print(f"Area of triangle is {x}")