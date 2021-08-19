# # WAP to check whether a number is prime or not.

# # def check_prime(no):
# #     if no <= 1:
# #         return False
# #     if no == 2 or no == 3:
# #         return True
# #     if no % 2 == 0 or no % 3 == 0:
# #         return False
    
    

# # no = int(input("Enter the no"))
x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 	101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
# 6k + 1 or 6k - 1
z = []
for no in range(500):
    if no <= 1:
        continue
    if no == 2 or no == 3:
        z.append(no)
        continue
    if no % 2 == 0 or no % 3 == 0:
        continue
    if no % 6 == 5 or no % 6 == 1:
        i = 5
        flag = False
        if i % 2 != 0:
            while i * i <= no:
                if no % i == 0:
                    flag = True
                    break
                i += 1
            if flag:
                continue
        z.append(no)
t = []
for i in range(min(len(x), len(z))):
    t.append((x[i], z[i]))
print(t)
