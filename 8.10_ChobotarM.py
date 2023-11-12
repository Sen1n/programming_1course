from itertools import permutations


def permutation(n):
    numbers = list(range(1, n + 1))
    perm_list = list(permutations(numbers))

    for perm in perm_list:
        print(" ".join(map(str, perm)))


n = int(input())
permutation(n)
# Chat GBT поміг, бо я взагалі не знаю як то робити, єдина ідея, що в мене була -
# спочатку порахувати к-сть перестановок, яка = n!, а потім якось через рядок або ліст
# зробити цикл, який би перевіряв чи є вже такий список, і якщо є, то робив новий, поки не вичерпається
# кількість перестановок, яка для 3 = 6
