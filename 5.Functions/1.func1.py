# WAP to demonstrate all four categories of functions for volume of the cylinder     
# (volume of    cylinder: 3.14*r*r*h)    
# a) Function without parameters without return value.    
# b) Function with parameter without return value.    
# c) Function without parameter with return value.    
# d) Function with parameters with return value

print("\nfunc_without_para_and_return")
def func_without_para_and_return():
    r = 4
    h = 10
    vol = 3.14 * r * r * h
    print(f"Volume of cylinder have radius {r} and height {h}: {round(vol, 2)}")
    
func_without_para_and_return()

print("\nfunc_with_para_and_no_return")
def func_with_para_and_no_return(r, h):
    vol = 3.14 * r * r * h
    print(f"Volume of cylinder have radius {r} and height {h}: {round(vol, 2)}")

r = 4
h = 10
func_with_para_and_no_return(r, h)

print("\nfunc_without_para_and_with_return")
def func_without_para_and_with_return():
    r = 4
    h = 10
    vol = 3.14 * r * r * h
    return f"Volume of cylinder have radius {r} and height {h}: {round(vol, 2)}"
x = func_without_para_and_with_return()
print(x)


def func_with_para_and_return(r, h):
    vol = 3.14 * r * r * h
    return f"Volume of cylinder have radius {r} and height {h}: {round(vol, 2)}"

print("\nfunc_with_para_and_return")
r = 4
h = 10
x = func_with_para_and_return(r, h)
print(x)