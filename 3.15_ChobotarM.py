k = int(input())
n = int(input())
i = 1
sum_digit = 0
while n > 0:
    bit = n % 10
    new_d = bit * (k ** (i - 1))
    i += 1
    sum_digit += new_d
    n //= 10
print(sum_digit)
