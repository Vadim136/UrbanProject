class Vehicle():

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


    def __init__(self, owner,  model, color, engine_power):
        self.owner = owner
        self. __model =  model
        self.__engine_power = engine_power
        color_lower = color.lower()
        if color_lower in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = color
        else:
            print(f"Такого цвета нет: {color}")
            self.__color = None

    def get_model(self):
        return f'Модель: {self.__model}'
    
    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'
    
    def get_color(self):
        return f'Цвет: {self.__color}'
    
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        color_lower = new_color.lower()
        if color_lower in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Такого цвета нет: {new_color}")

    pass

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    
    def get_passengers_limit(self):
        return f'Лимит пассажиров: {self.__PASSENGERS_LIMIT}'


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# print(vehicle1.get_passengers_limit()) проверка метода класса Sedan с выводом количества пассажиров