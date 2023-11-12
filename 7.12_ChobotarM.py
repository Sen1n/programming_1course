def binary_dig(number):
    count = 0
    while number > 0:
        remainder = number % 2
        number //= 2
        if remainder == 1:
            count += 1
    return count


n, m = [int(el) for el in input().split()]
summ = 0

for i in range(n, m + 1):
    summ += binary_dig(i)

print(summ)
