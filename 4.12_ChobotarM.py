"""На вході програми маємо послідовність цілих чисел, що закінчується числом 0.
Потрібно знайти суму парних чисел в даній послідовності, не враховуючи останнього нуля.

Вхідні дані
Послідовність цілих чисел, по одному числу в кожному рядку.

Вихідні дані
Одне число - сума парних чисел в послідовності."""
summ = 0
while True:
    n = int(input())
    if n != 0 and n % 2 == 0:
        summ += n
    elif n == 0:
        break
print(summ)
