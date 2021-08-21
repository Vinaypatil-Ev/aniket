# Write a C program to compute sum of diagonal elements of an array

def trace(matrix):
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                s += matrix[i][j]
    return s
                
                
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 2, 1],
        [5, 4, 2],
    ]
    
    x = trace(matrix)
    print(f"Sum of diagonal ele is {x}")