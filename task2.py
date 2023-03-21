# ✔ Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result_matrix = []
    ziped_rows = zip(*matrix)
    for row in ziped_rows:
        result_matrix.append(list(row))
    return result_matrix

matrix = [[8, 5, 4, 1], [3, 2, 9, 7]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()
print()    
transp_matrix = transpose_matrix(matrix)           
for i in range(len(transp_matrix)):
    for j in range(len(transp_matrix[0])):
        print(transp_matrix[i][j], end=' ')
    print()