'''За значенням n! (n! = 1 * 2 * ... * (n - 1) * n) визначити значення n.

Вхідні дані
Значення n! (1 ≤ n ≤ 2000).

Вихідні дані
Вивести натуральне число n.'''
n = int(input())
res_sum = 1
x = 1
for i in range(1, n + 1):
    n = n // i
    if n % (i + 1) != 0:
        break
    res_sum += 1
print(res_sum)