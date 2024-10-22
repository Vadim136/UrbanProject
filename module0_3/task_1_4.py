my_string = input('Введите строку: ')

length = len(my_string)

# определяем слово которое будет написанно при выводе сообщения
if length % 10 == 1 and length % 100 != 11:
    word = 'символ'
elif 2 <= length % 10 <= 4 and (length % 100 < 10 or length % 100 >= 20):
    word = 'символа'
else:
    word = 'символов'

print('В этой строке', length, word)

print('Введенная строка в верхнем регистре: ', my_string.upper())
print('Введенная строка в нижнем регистре: ', my_string.lower())
print('Введенная строка без пробелов: ', my_string.replace( ' ', ''))
print('Первый символ строки: ', my_string[0])
print('Последний символ строки: ', my_string[length-1])
