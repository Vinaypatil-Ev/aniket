# WAP to accept five subject marks and find out total and average of the marks
print("Enter five sub marks")
marks = []
for i in range(5):
    a = int(input(f"Enter marks of sub {i+1}: "))
    marks.append(a)
    
avg = sum(marks) / len(marks)

print(f"Your avg marks are {avg}")
