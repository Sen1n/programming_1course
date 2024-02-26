import math


class Vector:
    def __init__(self, *args):
        self.coordinates = list(args)

    def __str__(self):
        return f"Vector: {self.coordinates}"

    def dimension(self):
        return len(self.coordinates)

    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.coordinates))

    def mean(self):
        return sum(self.coordinates) / len(self.coordinates)

    def max_component(self):
        if not self.coordinates:
            return -math.inf
        return max(self.coordinates)

    def min_component(self):
        if not self.coordinates:
            return math.inf
        return min(self.coordinates)


def read_vectors_from_file(filename):
    vectors = []
    with open(filename, 'r') as file:
        for line in file:
            coordinates = [float(coord) for coord in line.split()]
            vectors.append(Vector(*coordinates))
    return vectors


def vector_with_max_dimension_and_min_length(vectors):
    max_dim_vectors = [v for v in vectors if v.dimension() == max(v.dimension() for v in vectors)]
    min_length_vector = min(max_dim_vectors, key=lambda x: x.length())
    return min_length_vector


def vector_with_max_length_and_min_dimension(vectors):
    max_length_vectors = [v for v in vectors if v.length() == max(v.length() for v in vectors)]
    min_dim_vector = min(max_length_vectors, key=lambda x: x.dimension())
    return min_dim_vector


def average_length(vectors):
    total_length = sum(v.length() for v in vectors)
    return total_length / len(vectors)


def count_vectors_above_average_length(vectors):
    avg_length = average_length(vectors)
    return sum(1 for v in vectors if v.length() > avg_length)


def vector_with_max_max_component_and_min_min_component(vectors):
    max_max_component_vector = max(vectors, key=lambda x: x.max_component())
    min_min_component_vector = min(vectors, key=lambda x: x.min_component())
    return max_max_component_vector, min_min_component_vector


# Створимо список імен файлів, які потрібно обробити
input_files = ["input01.txt", "input02.txt", "input03.txt"]

# Цикл для обробки кожного файлу
for filename in input_files:
    print(f"Results for {filename}:")

    # Читаємо дані з поточного файлу
    vectors = read_vectors_from_file(filename)

    # Знаходимо вектори згідно з умовою для поточного файлу
    result_max_dim_min_length_vector = vector_with_max_dimension_and_min_length(vectors)
    result_max_length_min_dim_vector = vector_with_max_length_and_min_dimension(vectors)
    result_avg_length = average_length(vectors)
    result_count_above_avg_length = count_vectors_above_average_length(vectors)
    result_max_max_component_vector, result_min_min_component_vector = vector_with_max_max_component_and_min_min_component(
        vectors)

    # Друкуємо результати для поточного файлу
    print("Vector with maximum dimension and minimum length:", result_max_dim_min_length_vector)
    print("Vector with maximum length and minimum dimension:", result_max_length_min_dim_vector)
    print("Average length of vectors:", result_avg_length)
    print("Number of vectors above average length:", result_count_above_avg_length)
    print("Vector with maximum maximum component and minimum minimum component:", result_max_max_component_vector)
    print("Vector with minimum minimum component and maximum maximum component:", result_min_min_component_vector)
    print()  # Додаємо порожній рядок між результатами різних файлів
