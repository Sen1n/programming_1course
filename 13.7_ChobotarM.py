"""13.7.
Дано текстовий файл. Групи символів, які відокремлені пропусками (одним або декількома)
і не містять пропусків усередині, будемо називати словами. Скласти підпрограми для:
a)    знаходження найдовшого слова у файлі;
b)    визначення кількості слів у файлі;
c)    вилучення з файла зайвих пропусків та всіх слів, що складаються з однієї букви;
d)    вилучення всіх пропусків на початку рядків, у кінці рядків та між словами (окрім одного);
e)    вставки пропусків у рядки рівномірно між словами так, щоб довжина всіх рядків
(якщо в них більше 1 слова) була 80 символів та кількість пропусків між словами
в одному рядку відрізнялась не більше, ніж на 1
(вважати, що рядки файла мають не більше, ніж 80 символів).
Результат записати у файл H."""


def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        if not words:
            return "No words in the file"
        longest_word = max(words, key=len)
        return longest_word


def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)


def remove_extra_spaces_and_short_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        filtered_words = [word for word in words if len(word) > 1]
        result = ' '.join(filtered_words)
        with open('13.7_txt', 'w') as output_file:
            output_file.write(result)


def remove_spaces(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        formatted_lines = [line.strip() for line in lines]
        result = ' '.join(formatted_lines)
        with open('13.7_txt', 'w') as output_file:
            output_file.write(result)


def insert_spaces(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        formatted_lines = []
        for line in lines:
            words = line.split()
            total_spaces = 80 - sum(len(word) for word in words)
            spaces_between_words = total_spaces // (len(words) - 1) if len(words) > 1 else 0
            formatted_line = (' ' * spaces_between_words).join(words)
            formatted_lines.append(formatted_line)
        result = '\n'.join(formatted_lines)
        with open('13.7_txt', 'w') as output_file:
            output_file.write(result)


file_path = '13.7_txt'

longest_word = find_longest_word(file_path)
print(f"The longest word is: {longest_word}")

word_count = count_words(file_path)
print(f"The number of words in the file is: {word_count}")

remove_extra_spaces_and_short_words(file_path)

remove_spaces(file_path)

insert_spaces(file_path)
