def input_matrix(n, m):
    mat = []
    for i in range(n):
        row = [int(el) for el in input(f"Пліз, уведіть {i + 1}-ий рядок\n--> ").split()]
        assert len(row) == m, f"Ви ввели некоректні дані, рядок повинен мати {m} елементів"
        mat.append(row)
    return mat


def print_matrix(mat):
    for row in mat:
        print(row)


def matrix_multiplication(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat2[0])):
            elem = 0
            for k in range(len(mat2)):
                elem += mat1[i][k] * mat2[k][j]
            row_result.append(elem)
        result.append(row_result)
    return result


def matrix_vector_multiplication(mat, vector):
    result = []
    for i in range(len(mat)):
        element = 0
        for j in range(len(vector)):
            element += mat[i][j] * vector[j]
        result.append(element)
    return result


def vector_matrix_multiplication(vector, mat):
    result = []
    for j in range(len(mat[0])):
        element = 0
        for i in range(len(vector)):
            element += vector[i] * mat[i][j]
        result.append(element)
    return result


def swap_rows(mat, i, j):
    mat[i], mat[j] = mat[j], mat[i]


def swap_columns(mat, i, j):
    for row in mat:
        row[i], row[j] = row[j], row[i]


def get_row(mat, i):
    return mat[i]


def scalar_vector_multiplication(scalar, vector):
    return [scalar * el for el in vector]


def subtraction_vector_from_matrix(mat, vector):
    result = []
    for i in range(len(mat)):
        row_result = [mat[i][j] - vector[j] for j in range(len(vector))]
        result.append(row_result)
    return result


if __name__ == "__main__":
    # 1) Введення матриць
    n1, m1 = [int(el) for el in input("Пліз, уведіть матрицю А, розміру (n, m):\n--> ").split()]
    assert n1 == m1, "Матриця повинна бути квадратною"
    mat_A = input_matrix(n1, m1)

    n2, m2 = [int(el) for el in input("Пліз, уведіть матрицю B, розміру (n, m):\n--> ").split()]
    assert n2 == m2, "Матриця повинна бути квадратною"
    mat_B = input_matrix(n2, m2)

    # 2) Виведення матриць
    print("Матриця A:")
    print_matrix(mat_A)

    print("\nМатриця B:")
    print_matrix(mat_B)

    # 3) Множення матриць
    result_matrix_product = matrix_multiplication(mat_A, mat_B)
    print("\nМатриця A * Матрицю B:")
    print_matrix(result_matrix_product)

    # 4) Множення матриці на вектор
    vector_input = [int(el) for el in input("Будь ласка, уведіть координати вектора:\n--> ").split()]
    result_matrix_vector_product = matrix_vector_multiplication(mat_A, vector_input)
    print("\nМатриця А * Вектор:")
    print(result_matrix_vector_product)

    # 5) Множення вектора на матрицю
    result_vector_matrix_product = vector_matrix_multiplication(vector_input, mat_A)
    print("\nВектор * Матриця A:")
    print(result_vector_matrix_product)

    # 6) Переставлення рядків та стовпчиків матриці
    row_index1, row_index2 = map(int, input("Уведіть через пробіл індекси рядків, що хочете поміняти:\n--> ").split())
    swap_rows(mat_A, row_index1 - 1, row_index2 - 1)
    print("\nМатриця після зміни рядків:")
    print_matrix(mat_A)

    # 7) Переставляння стовпчиків матриці
    col_index1, col_index2 = map(int, input("Уведіть через ' ' індекси стовпчиків, що хочете поміняти:\n--> ").split())
    swap_columns(mat_A, col_index1 - 1, col_index2 - 1)
    print("\nМатриця після зміни стовпчиків:")
    print_matrix(mat_A)

    # 8) Отримання рядка матриці
    row_index = int(input("Уведіть індекс рядка, що хочете отримати:\n--> "))
    selected_row = get_row(mat_A, row_index - 1)
    print(f"\nОтриманий рядок {row_index} Матриці A:")
    print(selected_row)

    # 9) Множення вектора на число
    scalar = int(input("Уведіть число, на яке множитимете вектор:\n--> "))
    result_scalar_vector_product = scalar_vector_multiplication(scalar, vector_input)
    print(f"\nСкаляр * наш вектор: {result_scalar_vector_product}")

    # 10)Віднімання вектора від всіх рядків матриці
    result_subtraction_vector = subtraction_vector_from_matrix(mat_A, vector_input)
    print("\nМатриця А - наш вектор від усіх рядків:")
    print_matrix(result_subtraction_vector)
