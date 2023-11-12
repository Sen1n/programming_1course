def ncd(a, b):
    while b:
        a, b = b, a % b
    return a


def nck(a, b):
    min_cr = a * b // ncd(a, b)
    return min_cr


A, B = [int(el) for el in input().split()]
count = 0
for P in range(A, B + 1):
    for Q in range(A, B + 1):
        if ncd(P, Q) == A and nck(P, Q) == B:
            count += 1
print(count)
