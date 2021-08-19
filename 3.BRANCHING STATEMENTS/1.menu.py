def cal_square():
    print("calculating square and cube")
    no = int(input("Enter the no: "))
    print(f"square of {no} : {no ** 2}")
    print(f"cube of {no} : {no ** 3}")

def check_leap_year():
    print("checking whether year is leap or not")
    y = int(input("Enter the year: "))
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f"{y} is leap year")
            else:
                print(f"{y} is not leap year")
        else:
            print(f"{y} is leap year")
    else:
        print(f"{y} is not leap year")


choice_switch = {1: cal_square, 2: check_leap_year}
choice = int(input("Enter your choice 1/2: "))
while choice != 1 and choice != 2 and choice != -1:
    print("Please enter the correct choice from 1/2")
    choice = int(input("choice: "))
choice_switch[choice]()
