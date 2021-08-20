def transpose(matrix):
    t = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j > t:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        t += 1



if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
           
           ]
    transpose(mat)
    print(mat)