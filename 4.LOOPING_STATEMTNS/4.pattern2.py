# WAP to print the following on output screen using jumping statements           
# 1         5          
# 2         4          
# 4         2          
# 5         1
n = 5
left = 0
right = n + 1
while left <n or right > 1:
    left += 1
    right -= 1
    if left == 3 or right == 3:
        continue
    print(left, right)
    