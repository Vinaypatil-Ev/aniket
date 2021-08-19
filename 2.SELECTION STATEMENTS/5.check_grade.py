# WAP a program to accept Percentage from user and check the GRADE

def check_grade(per):
    if per > 70:
        return "A"
    elif per >= 60 and per <= 70:
        return "B+" 
    elif per >= 45 and per < 60:
        return "B" 
    elif per >= 35 and per < 45:
        return "C" 
    else:
        return "Fail"
    
per = float(input("Enter the percentage: "))
print(f"Your grade is {check_grade(per)}")