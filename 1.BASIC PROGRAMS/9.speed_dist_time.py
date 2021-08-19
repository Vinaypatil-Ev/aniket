# WAP which calculate speed for time and distance.
def cal_speed(d, t):
    return d / t


d = float(input("Enter the distance: "))
t = float(input("Enter the time taken: "))
x = cal_speed(d, t)
print(f"speed is {x}")