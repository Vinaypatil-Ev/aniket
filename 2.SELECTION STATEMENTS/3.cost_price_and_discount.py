# WAP to accept Cost Price from user and ask whether the user is a student or not. If the     user is student and cost price is greater than 500, give discount of 10% ELSE discount will be 5%. If user is not student and cost price is greater 500 then give discount of 8% ELSE discount will be 2%. (Take all inputs from USER)

def give_disco(std, cost):
    if std == "y" or std == "Y":
        if cost > 500:
            return 90/100 * cost
        else:
            return 95/100 * cost
    else:
        if cost > 500:
            return 92/100 * cost
        else:
            return 98/100 * cost

cost = int(input("enter your cost price: "))
std = input("Are you student y/n or Y/N: ")

x = give_disco(std, cost)
print(f"After giving discount on {cost} your final price is {x}")

