while True:
    n, m = [int(el) for el in input().split()]
    summ = 0

    if n < 0 and m < 0:
        break
    else:
        for el in range(n, m + 1):
            remainder = el % 10
            if remainder > 0:
                summ += remainder
            else:
                summ += el // 10
        if summ > 0:
            print(summ)
