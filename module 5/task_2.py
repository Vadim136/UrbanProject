
class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

    def __len__(self) :
        return self.number_of_floors
    
    def __str__(self) :
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

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

print(h1)
print(h2)

print(len(h1))
print(len(h2))