import inspect

def introspection_info(obj):
    return (f"'type': {type(obj).__name__},\n"
            f"'attributes': {[atr for atr in dir(obj) if not atr.startswith('__')]},\n"
            f"'methods': {[method for method in dir(obj) if method.startswith('__')]},\n"
            f"'module': {inspect.getmodule(introspection_info).__name__}\n")


number_info_1 = introspection_info(42)
print(number_info_1)


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

number_info_2 = introspection_info(h1)
print(number_info_2)

number_info_3 = introspection_info([42, 44, 45, 46])
print(number_info_3)
