def unique_digits(number):
    uniq_digits = []
    while number > 0:
        digit = number % 10
        if digit in uniq_digits:
            return False
        uniq_digits.append(digit)
        number //= 10
    return True


n, m = [int(el) for el in input().split()]
lst_n = []

for i in range(n, m + 1):
    if unique_digits(i):
        lst_n.append(i)

print(*lst_n)
