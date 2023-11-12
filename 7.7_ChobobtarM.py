def nsd(a, b):
    while b:
        a, b = b, a % b
    return a


def min_crate(n):
    nsk = 1
    for i in range(2, n + 1):
        nsk = (nsk * i) // nsd(nsk, i)
    return nsk


n = int(input())
print(min_crate(n))
