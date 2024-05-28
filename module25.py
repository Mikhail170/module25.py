def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for i in range(m):
            matrix[-1].append(value)
    return(matrix)
result1 = get_matrix(5,5,25)
result2 = get_matrix(4, 4, 50)
result3 = get_matrix(3, 3, 40)
print(result1)
print(result2)
print(result3)