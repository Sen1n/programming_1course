""" Для заданого натурального числа n виведіть його найбільший дільник, відмінний від n.

%Вхідні дані
Одне натуральне число

Вихідні дані
Виведіть найбільший дільник числа
n, відмінний від n.

Приклад
Вхідні дані #1 content_copy 21
Вихідні дані #1 content_copy 7 """
n = int(input())
lst = []
for i in range(1, n):
    if n % i == 0:
        lst.append(i)
print(lst[-1])
