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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other
        else:
            return f'Ошибка, введите целое число'

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return f'Ошибка, введите целое число'

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return f'Ошибка, введите целое число'

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return f'Ошибка, введите целое число'

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            return f'Ошибка, сравнение невозможно'

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f'Ошибка, сравнение невозможно'

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            return f'Ошибка, сравнение невозможно'

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f'Ошибка, сравнение невозможно'

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            return f'Ошибка, сравнение невозможно'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
