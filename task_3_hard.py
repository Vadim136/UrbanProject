def calculate_structure_sum(data):
    def recursive_sum(element):
        if isinstance(element, (int, float)):
            return element
        elif isinstance(element, str):
            return len(element)
        elif isinstance(element, dict):
            return sum(recursive_sum(key) + recursive_sum(value) for key, value in element.items())
        elif isinstance(element, (list, tuple, set)):
            return sum(recursive_sum(item) for item in element)
        else:
            return 0

    return recursive_sum(data)

# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)  # Вывод: 99
