
class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого этажа нет в "{self.name}"')
        else:
            for i in range(1, new_floor):
                print(i)
            print(f'Вы на {new_floor} в "{self.name}"')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h1.go_to(15)