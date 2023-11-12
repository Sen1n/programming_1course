def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_lucky_prime(n):
    reversed_n = int(str(n)[::-1])
    return is_prime(n) and is_prime(reversed_n) and n != reversed_n


def find_kth_lucky_prime(K):
    count = 0
    n = 2
    while n <= 10 ** 6:
        if is_lucky_prime(n):
            count += 1
            if count == K:
                return n
        n += 1
    return -1


K = int(input())
result = find_kth_lucky_prime(K)
print(result)
