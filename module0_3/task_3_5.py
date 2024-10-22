def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        first = int(str_number[0])
        if first == 0:
            return 1
        return int(str_number)
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(103200))  # Ожидаемый вывод: 6


