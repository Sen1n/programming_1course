a, b, c = [int(d) for d in input().split()]
D = (b ** 2) - (4 * a * c)

if D < 0:
    print("No roots")
elif D == 0:
    x1 = -b / (2 * a)
    print("One root:", x1)
else:
    x1 = int((-b + (D ** 0.5)) / (2 * a))
    x2 = int((-b - (D ** 0.5)) / (2 * a))
    print("Two roots:", min(x1, x2), max(x1, x2))
