def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    tests = int(input())

    for _ in range(tests):
        n, m = map(int, input().split())

        # Обчислюємо F(n) та F(m)
        fn = fibonacci(n)
        fm = fibonacci(m)

        # Знаходимо НСД(F(n), F(m))
        result = gcd(fn, fm) % 10 ** 8

        print(result)


if __name__ == "__main__":
    main()
# прикол у тому, що в задачі немає точної к-сті введень, які треба, то я не знаю шо робить.
#  пан Креневич показав нам спосіб через файл.опен ес, але я не дуже розумію :(
