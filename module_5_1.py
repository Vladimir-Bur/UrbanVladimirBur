class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'\nЖилмассив: "{self.name}", всего этажей - {self.number_of_floors}')
        if 1 <= new_floor <= self.number_of_floors:
            for number_of_floor in range(1, new_floor + 1):
                print(number_of_floor)
                number_of_floor += 1
            print(f'Вы прибыли на этаж № {new_floor}.')
        else:
            print(f'"У нас этажа № {new_floor} не существует!"')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
