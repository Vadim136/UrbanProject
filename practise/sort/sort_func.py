nums = [2, 3, 5, 7, 8, 9, 4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True

# bubble_sort(nums)
# print(nums)


def selection_func(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


# selection_func(nums)
# print(nums)

def insertion_sort(ls):
    # Проходим по всем элементам массива, начиная со второго элемента
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        # Перемещаем элементы массива, которые больше key, на одну позицию вправо
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        # Вставляем key на правильное место
        ls[j + 1] = key
    return ls

# insertion_sort(nums)
# print(nums)