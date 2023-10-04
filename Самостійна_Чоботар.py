# задача: задано n, Знайти добуток усіх чисел від 1 до н включно, які діляться на 8
n = int(input())
multiply = 1
for i in range(1, n + 1):
    if i % 8 == 0:
        multiply *= i
print(multiply)
