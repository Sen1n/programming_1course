alphabet = "0123456789ABCD"
str_thirteen = ""
n = int(input())

while n > 0:
    remainder = n % 13
    str_thirteen = alphabet[remainder] + str_thirteen
    n //= 13

print(str_thirteen)
