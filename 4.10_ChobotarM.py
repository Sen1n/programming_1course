"""Вивести відповідь до задачі, враховуючи, що n — номер варіанту.

n=1 : Обчислити суму трьохзначних чисел, цифри яких парні.

n=2 : Обчислити кількість трьохзначних чисел, цифри яких зростають.

n=3 : Обчислити суму трьохзначних чисел, цифри яких непарні.

n=4 : Обчислити кількість трьохзначних чисел, цифри яких спадають.

n=5 : Обчислити суму трьохзначних чисел, які дорівнюють сумі кубів своїх цифр.

n=6 : Обчислити кількість трьохзначних чисел, цифри яких різні."""
n = int(input())
counter = 0
summ = 0
for i in range(100, 1000, 2):
    for g in str(i):
        if int(g) % 2 == 0:
            counter += 1
    if counter == 3:
        summ += i
    counter = 0

    # start 2 level

count_2 = 0

for i in range(100, 1000):
    if (str(i))[0] < (str(i))[1] and (str(i))[1] < (str(i))[2]:
        count_2 += 1

# 3 level

counter_3 = 0
summ_3 = 0
for i in range(100, 1000):
    for g in str(i):
        if int(g) % 2 != 0:
            counter_3 += 1
    if counter_3 == 3:
        summ_3 += i
    counter_3 = 0

# start lvl 4

count_4 = 0

for i in range(100, 1000):
    if (str(i))[0] > (str(i))[1] and (str(i))[1] > (str(i))[2]:
        count_4 += 1

# start lvl 5
summ_5 = 0
for i in range(100, 1000):
    if ((int((str(i))[0])) ** 3) + ((int((str(i))[1])) ** 3) + ((int((str(i))[2])) ** 3) == i:
        summ_5 += i

# lvl 6

counter_6 = 0
for i in range(100, 1000):
    if str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2]:
        counter_6 += 1
if n == 1:
    print(summ)
elif n == 2:
    print(count_2)
elif n == 3:
    print(summ_3)
elif n == 4:
    print(count_4)
elif n == 5:
    print(summ_5)
elif n == 6:
    print(counter_6)
