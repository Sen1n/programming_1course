"""14.9.
У папці з програмою міститься набір текстових файлів, кожен з яких містить набір дійсних чисел.
Крім цього, у цій же папці міститься файл content.txt, що містить перелік імен файлів.
Реалізуйте програму, що:
    підсумовує дані, з файлів, що вказані у файлі content.txt;
    коректно опрацьовує ситуацію, у випадку якщо файл content.txt
    не існує за вказаним розташуванням або не доступний для читання та виводить на екран відповідне повідомлення;
    коректно опрацьовує ситуацію, у випадку якщо файл з переліку зазначеного у файлі content.txt не існує за вказаним
    розташуванням або не доступний для читання;
    коректно опрацьовує ситуацію, якщо файл з переліку зазначеного у файлі content.txt містить не лише дійсні числа."""
try:
    with open("content.txt", "rt") as content_file:
        file_list = content_file.read().splitlines()

    for file_name in file_list:
        try:
            with open(file_name, "rt") as data_file:
                data = [float(line.strip()) for line in data_file.readlines()]


        except FileNotFoundError:
            print(f"файл '{file_name}' не знайдено.")
        except IOError:
            print(f"помилка зчитування файлу '{file_name}'.")
        except ValueError:
            print(f"файл '{file_name}' містить дані, що не є числовими.")
except FileNotFoundError:
    print("файл 'content.txt' не існує.")
except IOError:
    print("помилка читання файлу 'content.txt'.")
