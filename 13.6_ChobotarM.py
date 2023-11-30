def create_text_file(sequence, filename):
    with open("13.6_txt", 'w') as file:
        index = 0
        while index < len(sequence):
            line = sequence[index:index + 40]
            file.write(line + '\n')
            index += 40


sequence = input()
create_text_file(sequence, "13.6_txt")
