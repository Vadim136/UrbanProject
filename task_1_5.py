immutable_var = 1, 2, 3, 4
print('Кортеж - неизменяемый объект: ', immutable_var)
'''
immutable_var[0] = 3
    ~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
кортеж нельзя изменить, он нужен для хранения информации 
которую в процессе работы не хотелось бы изменять и он занимает
меньше места в памяти
''' 
mutable_list = [1, 'string', True]
print('Список - изменяемый объект: ', mutable_list)
mutable_list[0] = 2
mutable_list[1] = 'newString'
mutable_list[2] = False
mutable_list.append('newItem')
print('Измененный список: ', mutable_list)

print('Объем памяти занимаемой кортежем:', immutable_var.__sizeof__())
print('Объем памяти занимаемой списком:', mutable_list.__sizeof__())