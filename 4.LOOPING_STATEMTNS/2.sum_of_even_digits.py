# WAP to accept a number from user and find out sum of even digits from that given number


no = int(input("Enter the big no: "))
s = 0
while no != 0:
    t = no % 10
    if t % 2 == 0:
        s += t
    no //= 10
print(f"Sum of even digits {s}")
