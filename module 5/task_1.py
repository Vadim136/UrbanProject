
class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print(f'Такого этажа нет в "{self.name}"')
        else:
            print(f'Вы на {new_floor} в "{self.name}"')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h1.go_to(18)