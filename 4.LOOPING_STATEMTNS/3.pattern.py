# WAP to print the following pattern 
#     * 
#    ***                   
#   *****                 
#  *******               
# *********
n = 5
z = 1
for i in range(5):
    for j in range(n + i+z):
        if j < n:
            print(end=" ")
        else:
            print("*", end="")
    n -= 1
    z += 1
    print()