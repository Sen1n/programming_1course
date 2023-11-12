def is_palindrome(s):
    return s == s[::-1]


n = int(input())
found_bases = []
for base in range(2, 37):
    number_in_base = ""
    num = n
    while num > 0:
        digit = num % base
        if digit < 10:
            number_in_base = str(digit) + number_in_base
        else:
            number_in_base = chr(ord('a') + digit - 10) + number_in_base
        num //= base
    if is_palindrome(number_in_base):
        found_bases.append(base)

if len(found_bases) == 0:
    print("none")
elif len(found_bases) == 1:
    print("unique")
    print(*found_bases)
else:
    print("multiple")
    print(" ".join(map(str, found_bases)))
