class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin = Car.__is_valid_vin(self)
        self.__numbers = Car.__is_valid_numbers(self)

    def __is_valid_vin(self):
        self.vin_number = self.__vin
        if not isinstance(self.vin_number, int):
            raise IncorrectVinNumber(f'Некорректный тип vin номер')
        if not 1000000 <= self.vin_number <= 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        else:
            self.vin_number = True

    def __is_valid_numbers(self):
        self.numbers = self.__numbers
        if not isinstance(self.numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера')
        else:
            self.numbers = True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
