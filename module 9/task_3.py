
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list(len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))

second_result = list( True if len(first[i])==len(second[i]) else False for i in range(len(first)))

print(first_result)
print(second_result)
