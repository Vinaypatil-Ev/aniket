def peri_sq(side):
    return 4 * side

def peri_rect(a, b):
    return 2 * (a + b)


side = float(input("Side of square: "))
x = peri_sq(side)
print(f"Perimeter of square is {x}")
a = float(input("Enter Length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
y = peri_rect(a, b)
print(f"Perimeter of rectangle is {y}")
