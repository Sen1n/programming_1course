"""
13.5.
Дано текстовий файл, компоненти якого є цілими числами. Скласти підпрограми для обчислення:
a)    кількості парних чисел серед компонент;
b)    кількості квадратів непарних чисел серед компонент;
c)    різниці між найбільшим парним і найменшим непарним числами з компонент;
d)    кількості компонент у найдовшій зростаючій послідовності компонент файла.
"""
with open("13.5_txt", "r", encoding='utf-8') as file:
    file_reading = file.read()


def even_dig_c():
    counter = 0
    for line in file_reading.split():  # розділити рядок на окремі числа
        if int(line) % 2 == 0:
            counter += 1
    return counter


print(even_dig_c())


def square_odd():
    counter = 0
    for line in file_reading.split():
        num = int(line)
        if num % 2 != 0:
            square = num ** 2
            if str(square) in file_reading:
                counter += 1
    return counter


print(square_odd())


# різниця між найбільшим парним і найменшим непарним числами з компонент
def difference():
    a = float("-inf")
    b = float("inf")
    for line in file_reading.split():
        if int(line) % 2 == 0:
            if int(line) > a:  # одразу виникає проблема, коли число менше як 0 ------ по ідеї додавши інф тепер пропало
                a = int(line)
        elif int(line) < b:
            b = int(line)

    return a - b


print(difference())


# кількості компонент у найдовшій зростаючій послідовності компонент файла.
def increasing_sequence():
    current_seq = []
    max_seq = []
    prev_num = float('-inf')

    for line in file_reading.split():
        num = int(line)

        if num > prev_num:
            current_seq.append(num)
        else:
            current_seq = [num]

        if len(current_seq) > len(max_seq):
            max_seq = current_seq.copy()

        prev_num = num

    return len(max_seq)


print(increasing_sequence())
