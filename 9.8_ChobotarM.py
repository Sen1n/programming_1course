# b = int(input())
# n = [int(el) for el in input().split()]
# n.sort()
# n = set(n)
# n.discard(0)
# print(len(set(n)))

b = int(input())
n = [abs(int(el)) for el in input().split()]
print(len(set(n)))
