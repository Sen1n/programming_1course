''' Знайти суму парних цифр натурального числа n.

Вхідні дані
Натуральне число n.

Вихідні дані
Сума парних цифр числа n або -1, якщо такі цифри відсутні.'''

n = int(input())
i = 1
res_sum_par = 0
while 10 ** (i - 1) <= n:
    digit = (n % 10 ** i) // 10 ** (i - 1)
    i += 1
    if digit % 2 == 0:
        res_sum_par += digit
if res_sum_par == 0:
    print("-1")
else:
    print(res_sum_par)
