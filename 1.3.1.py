from math import pi
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        s_squared = p * (p - self.a) * (p - self.b) * (p - self.c)
        if s_squared < 0:
            return 0
        return sqrt(s_squared)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return (self.a + self.b) * 0.5 * self.d


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)


def read_file(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            figure_type = parts[0]
            parameters = list(map(float, parts[1:]))
            if figure_type == 'Triangle':
                figures.append(Triangle(*parameters))
            elif figure_type == 'Rectangle':
                figures.append(Rectangle(*parameters))
            elif figure_type == 'Trapeze':
                figures.append(Trapeze(*parameters))
            elif figure_type == 'Parallelogram':
                figures.append(Parallelogram(*parameters))
            elif figure_type == 'Circle':
                figures.append(Circle(*parameters))
    return figures


def find_largest_area_and_perimeter(figures):
    max_area = 0
    max_perimeter = 0
    largest_area_figure = None
    largest_perimeter_figure = None

    for figure in figures:
        area = figure.area()
        perimeter = figure.perimeter()
        if area > max_area:
            max_area = area
            largest_area_figure = figure
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            largest_perimeter_figure = figure

    return largest_area_figure, largest_perimeter_figure


def main():
    filename = input("Enter the filename: ")
    figures = read_file(filename)
    largest_area_figure, largest_perimeter_figure = find_largest_area_and_perimeter(figures)
    print("Figure with the largest area:", largest_area_figure.__class__.__name__)
    print("Area:", largest_area_figure.area())
    print("Figure with the largest perimeter:", largest_perimeter_figure.__class__.__name__)
    print("Perimeter:", largest_perimeter_figure.perimeter())


if __name__ == "__main__":
    main()
