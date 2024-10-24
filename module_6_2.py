class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'\n{Vehicle.get_model(self)}, '
              f'\n{Vehicle.get_horsepower(self)}, '
              f'\n{Vehicle.get_color(self)}'
              f'\nВладелец: {str(self.owner)}')

    def set_color(self, new_color : str):
        self.new_color = new_color
        if self.new_color.lower() in Vehicle._COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'\nНельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    pass

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
