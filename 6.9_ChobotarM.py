a = input()
suma = 0
for el in a:
    if el in ["+", "-", "*", "/", "%"]:
        suma += 1

power = a.count('**')
int_part = a.count('//')
suma -= (power + int_part)

print(suma)
