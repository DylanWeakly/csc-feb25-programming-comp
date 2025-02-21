def matrix():
    matrixs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    i = 0
    length = len(matrixs)
    arr = []

    for row in matrixs:
        new_row = []
        for row in matrixs:
            new_row.append(row[i])
        arr.append(new_row)
        i += 1
    return arr

print(matrix())