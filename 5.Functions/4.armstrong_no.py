def armstrong_no(no):
    t = 0
    n = no
    while n != 0:
        t += (n % 10) ** 3
        n //= 10
    if t == no:
        return True
    return False


no = int(input("Enter the no: "))
x = armstrong_no(no)
if x:
    print(f"{no} is armstrong")
else:
    print(f"{no} is not armstrong")