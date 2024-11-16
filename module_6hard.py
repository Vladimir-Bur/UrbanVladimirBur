import math

class Figure:
    sides_count = 0
    __sides = 0
    val_side = 0
    __color = [0, 0, 0]
    _perimeter = 0
    filled = None
    valid_color = True
    valid_sides = True
    def __init__(self, sides : int, color : [], filled):
        self.sides = sides
        self.__is_valid_sides()
        self.color = color
        self.__is_valid_color()
        self.filled = filled

    def get_color(self):
        return Figure.__color

    def __is_valid_color(self):
#        name_color = ['R', 'G', 'B']
        Figure.valid_color = True
        for i in range(3):
            if isinstance(self.color[i], int) and 0 <= self.color[i] <= 255:
                continue
            else:
#                print(f'\nДля Цвета "{name_color[i]}" введите целое число от 0 до 255 (включительно)')
#                print(f'Сейчас {name_color[i]} = {self.color[i]}')
                Figure.valid_color = False
                break

    def set_color(self, r, g, b):
        self.color = [r, g, b]
        Figure.__is_valid_color(self)
        if Figure.valid_color:
            Figure.__color = list(self.color)

    def __is_valid_sides(self): # Проверка стороны фигуры и возврат значения Figure.val_side = значению стороны фигуры и Figure.valid_sides = True или Figure.val_side = 1 и Figure.valid_sides = False.
        Figure.valid_sides = True
        Figure.sides_count = self.sides_count
        list_sides = [*self.sides]
        if len(list_sides) == 1:
            Figure.val_side = list_sides[0]
        elif len(list_sides) != Figure.sides_count:
            Figure.val_side = 1
            Figure.valid_sides = False
        else:
            Figure.val_side = list_sides[0]
            for side in range(len(list_sides) - 1):
                if list_sides[side] != list_sides[(side + 1)]:
                    Figure.val_side = 1
                    Figure.valid_sides = False
                    break

        if not isinstance(Figure.val_side, int):
            print(f'Сторона должна быть целым числом ')
            print(f'Сейчас {self.sides} ')
            Figure.valid_sides = False

    def get_sides(self):
        return Figure.__sides

    def __len__(self):
        self.perimetr = Figure.__sides[0] * Figure.sides_count
        return self.perimetr

    def set_sides(self, *new_sides):
        self.sides = [*new_sides]
        Figure.__is_valid_sides(self)
        if Figure.valid_sides:
            Figure.__sides = list(self.sides)

class Circle(Figure):
    sides_count = 1
    _color = [0, 0, 0]
    _sides = 0
    __radius = 0
    def __init__(self, color, *sides):
        super().__init__(sides, color, filled=None)

        if Figure.valid_color:
            Circle._color = list(self.color)
            super().set_color(*Circle._color)

        Circle._sides = Figure.val_side
        super().set_sides(Circle._sides)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if not Figure.valid_sides:
            super().set_sides(Circle.sides_count)

    def set_color(self, r, g, b):
        super().set_color(r, g, b)
        if Figure.valid_color:
            Circle._color = list(self.color)
            super().set_color(*Circle._color)
        else:
            super().set_color(*Circle._color)

    def get_square(self):
        Circle.__radius = Circle._sides / (2 * math.pi)
        square = math.pi * Circle.__radius ** 2
        return f'Площадь круга: {round(square, 2)}'

class Triangle(Figure):
    sides_count = 3
    _color = [0, 0, 0]
    _sides = []
    _square = 0

    def __init__(self, color, *sides):
        super().__init__(sides, color, filled=None)
        if Figure.valid_color:
            Triangle._color = list(self.color)
            super().set_color(*Triangle._color)

        Triangle._sides = []
        for s in range(3):
            Triangle._sides.append(Figure.val_side)
        super().set_sides(*Triangle._sides)

    def set_color(self, r, g, b):
        super().set_color(r, g, b)
        if Figure.valid_color:
            Triangle._color = list(self.color)
            super().set_color(*Triangle._color)
        else:
            super().set_color(*Triangle._color)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if Figure.valid_sides:
            new_list_sides = []
            for s in range(3):
                new_list_sides.append(Figure.val_side)
            Triangle._sides = new_list_sides
            super().set_sides(*new_list_sides)
        else:
            super().set_sides(*Triangle._sides)

    def get_square(self):
        p = (Triangle._sides[0] + Triangle._sides[1] + Triangle._sides[2])
        Triangle._square = math.sqrt((p * (p - Triangle._sides[0]) * (p - Triangle._sides[1]) * (p - Triangle._sides[2])))
        return f'Площадь треугольника: {round(Triangle._square, 2)}'

class Cube(Figure):
    sides_count = 12
    _color = [0, 0, 0]
    _sides = []
    _volume = 0
    def __init__(self, color, *sides):
        super().__init__(sides, color, filled=None)
        if Figure.valid_color:
            Cube._color = list(self.color)
            super().set_color(*Cube._color)

        Cube._sides = []
        for s in range(Cube.sides_count):
            Cube._sides.append(Figure.val_side)
        super().set_sides(*Cube._sides)

    def set_color(self, r, g, b):
        super().set_color(r, g, b)
        if Figure.valid_color:
            Cube._color = list(self.color)
            super().set_color(*Cube._color)
        else:
            super().set_color(*Cube._color)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if Figure.valid_sides:
            new_list_sides = []
            for s in range(Cube.sides_count):
                new_list_sides.append(Figure.val_side)
            Cube._sides = new_list_sides
            super().set_sides(*Cube._sides)
        else:
            super().set_sides(*Cube._sides)

    def get_volume(self):
        Cube._volume = Cube._sides[0] ** 3
        return Cube._volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print('Дополнительная проверка')
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(circle2.get_color())
print(circle2.get_sides())
print(len(circle2))
triangle2 = Triangle((200, 200, 100), 10, 6)
print(triangle2.get_color())
print(triangle2.get_sides())
print(len(triangle2))
cube2 = Cube((200, 200, 100), 9)
print(cube2.get_color())
print(cube2.get_sides())
print(len(cube2))
cube3 = Cube((200, 200, 100), 9, 12)
print(cube3.get_color())
print(cube3.get_sides())
print(len(cube3))