first = input('Введите первое число : ' )
second = input('Введите второе число : ' )
third = input('Введите третье число : ' )

if first == second and second == third and third == first:
    print('Все три числа равны!')
elif first == second or second == third or third == first:
    print('Два числа равны!')
else:
    print('Нет равных чисел!')
