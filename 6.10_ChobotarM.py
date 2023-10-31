string = input()
output_string = ""

for el in string:
    if el.isalpha() and el.islower():
        output_string += el * 2
    else:
        output_string += el
print(output_string)
