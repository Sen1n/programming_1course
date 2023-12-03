"""14.8.
До програми з клавіатури надходить послідовність цифр.
Послідовність задається доти, щоки користувач не введе слово «досить».
Слід зауважити, що користувач не є дисциплінованим і може заміть цифр вводити будь-що.
Якщо користувач вводить з клавіатури число більше за 9, то програма ініціює виключення RuntimeError.
Якщо користувач вводить число менше за 0, то програма ініціює виключення TypeError.
Якщо користувач вводить дійсне значення з діапазону від 0 до 9, то програма ініціює виключення ValueError.
Підрахувати кількість виключень кожного типу, що виникають у програмі."""

# lst = [str(el) for el in input().split() if el != "досить" or "Досить"]
stop = "досить"
seq_l = []
runtime_errors = 0
type_errors = 0
value_errors = 0

while True:
    sequence_el = input("Введіть число: ")

    if sequence_el.lower() == stop:
        break

    try:
        sequence_el = int(sequence_el)
    except ValueError:
        print("Потрібно задати ціле число!")
        continue

    try:
        if sequence_el > 9:
            raise RuntimeError("Ви ввели число більше 9")
        elif sequence_el < 0:
            raise TypeError("Ви ввели число менше 0")
        elif 0 <= sequence_el <= 9:
            raise ValueError("Значення числа в діапазоні від 0 до 9")
    except RuntimeError as e:
        runtime_errors += 1
        print(e)
    except TypeError as e:
        type_errors += 1
        print(e)
    except ValueError as e:
        value_errors += 1
        print(e)

print(f"Кількість виключень RuntimeError: {runtime_errors}")
print(f"Кількість виключень TypeError: {type_errors}")
print(f"Кількість виключень ValueError: {value_errors}")
