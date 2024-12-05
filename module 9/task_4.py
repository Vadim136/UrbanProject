
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda str1, str2: str1==str2 , first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

# Создание функции для записи в файл
write = get_advanced_writer('example.txt')

# Запись данных в файл
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



import random


class MysticBall():
    def __init__(self, *args):
        self.words = []
        for arg in args:
            self.words.append(arg)
        
        
    def __call__(self):
        return random.choice(self.words)
    
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())