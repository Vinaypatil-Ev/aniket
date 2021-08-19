# WAP to convert Fahrenheit temp in degree Celsius

def f_to_d(f):
    return (f - 32) * 5 / 9


f = float(input("Enter Fahrenheit temprature: "))
x = f_to_d(f)
print(f"{f} fahreheit is {round(x, 3)} degree celcius")

# round used above is to round the decimal values upto 3 digits
    