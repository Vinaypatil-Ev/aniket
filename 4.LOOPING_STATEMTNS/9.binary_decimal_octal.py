#  WAP to convert decimal to binary /binary to octal

no = int(input("Enter a No: "))
b = bin(no).replace("0b", "")
o = oct(no).replace("0o", "")
h = hex(no).replace("0x", "")
print(f"Binary of {no} is : {b}")
print(f"Octal of {no} is : {o}")
print(f"Hex of {no} is : {h}")