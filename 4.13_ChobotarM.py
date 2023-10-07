"""Знайти кількість двозначних чисел, які не змінюють свою суму цифр при множені числа на однозначне ціле число n (n = 0 .. 9).

Вхідні дані
Ціле число n (0 ≤ n ≤ 9).

Вихідні дані
Вивести шукану кількість двозначних чисел."""
n = int(input())
counter = 0
for i in range(10, 100):
    b = i * n
    if len(str(b)) == 3:
        if int(str(i)[0]) + int(str(i)[1]) == int(str(b)[0]) + int(str(b)[1]) + int(str(b)[2]):
            counter += 1
    elif len(str(b)) == 2:
        if int(str(i)[0]) + int(str(i)[1]) == int(str(b)[0]) + int(str(b)[1]):
            counter += 1
    else:
        break
print(counter)
