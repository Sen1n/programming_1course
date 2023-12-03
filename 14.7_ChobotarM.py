"""14.7.
Дано список чисел. Не використовуючи функцію len визначення кількості елементів
у цьому списку та не використовуючи цикл по колекції, визначити:
a)    кількість елементів у списку;
b)    суму елементів у списку;
c)    значення найбільшого відношення (частки) серед елементів."""


# a)
def length():
    l_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    if not l_1:
        return "Довжина списку = 0"
    elif l_1:
        while l_1:
            l_1.remove(l_1[0])
            counter += 1
    return counter


print(length())


# b)
def summ():
    l_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    summa = 0
    while l_2:
        summa += l_2[0]
        l_2.remove(l_2[0])
    return summa


print(summ())

# c)
l_3 = [1, 2, 3, 4, 5, 6, 7, 8]
k = length()
n = 0
max_frac = []
i = 0
a = float("-inf")
while k:
    fraction = l_3[0 + i] / l_3[0]
    if n > 0:
        fraction = l_3[0 + i] / l_3[n]
    if fraction > a:
        a = fraction
        max_frac.append(a)

    n += 1
    k -= 1
    if k == 0:
        n = 0
        i += 1
        k += length()
        if l_3[-1 + i] == length():
            break

print(max(max_frac))
