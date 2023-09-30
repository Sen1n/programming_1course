'''Задано натуральне число
�
n. Потрібно збільшити на
1
1 усі його парні цифри та зменшити на
1
1 усі його непарні цифри.'''

n = int(input())

new_n = 0
counter = 0
while n != 0:

    s = n % 10
    if s % 2 == 0:
        new_n += (s + 1) * (10 ** counter)
    else:
        new_n += (s - 1) * (10 ** counter)
    counter += 1
    n //= 10

print(new_n)
