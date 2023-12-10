from SW4_my_module import input_matrix, print_matrix, swap_rows


def upper_triangular(matrix):
    n = len(matrix)

    for i in range(n):
        # Перевірка чи елемент на головній діагоналі =0
        if matrix[i][i] == 0:
            print("Матриця не може бути перетворена у верхню трикутну, бо на головній діагоналі є нуль")
            return

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(n)]


def matrix_rank(matrix):
    # Копія матриці для збереження оригінальної матриці
    mat_copy = [row[:] for row in matrix]

    # Перетворення матриці у верхню трикутну форму
    upper_triangular(mat_copy)

    # Обчислення рангу як кількість ненульових рядків
    rank = sum(1 for row in mat_copy if any(row))

    return rank


def determinant(matrix):
    # Копія матриці для збереження оригінальної матриці
    mat_copy = [row[:] for row in matrix]

    # Перетворення матриці у верхню трикутну форму
    upper_triangular(mat_copy)

    # Обчислення визначника як добуток головних діагональних елементів
    det = 1
    for i in range(len(mat_copy)):
        det *= mat_copy[i][i]

    return det


# ТЕСТИ
if __name__ == "__main__":
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Тестування обчислення рангу матриці
    test_rank = matrix_rank(test_matrix)
    print(f"\nТест рангу матриці:\nРанг матриці: {test_rank}")

    # Тестування обчислення визначника матриці
    test_det_matrix = [
        [2, 3, 1],
        [0, 1, 4],
        [1, 1, 0]
    ]
    test_det = determinant(test_det_matrix)
    print(f"\nТест визначника матриці:\nВизначник матриці: {test_det}")

# if __name__ == "__main__":
#     n, m = [int(el) for el in input("Введіть розмір квадратної матриці (n, n):\n--> ").split()]
#     assert n == m, "Матриця повинна бути квадратною"
#     mat = input_matrix(n, m)
#
#     print("Початкова матриця:")
#     print_matrix(mat)
#
#     upper_triangular(mat)
#
#     print("\nМатриця після перетворення у верхню трикутну:")
#     print_matrix(mat)
#
#     rank = matrix_rank(mat)
#     print(f"\nРанг матриці: {rank}")
#     det = determinant(mat)
#
#     print(f"\nВизначник матриці: {det}")
