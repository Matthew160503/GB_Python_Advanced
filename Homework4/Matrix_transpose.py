# Напишите функцию для транспонирования матрицы.

def matrix_transpose(array: list):
    m_trans = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
    return m_trans


matrix = [[1, 2, 3], [3, 2, 1]]

print(matrix)
print(matrix_transpose(matrix))
