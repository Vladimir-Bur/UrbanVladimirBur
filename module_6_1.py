class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food.edible
        if self.food == Fruit.edible:
            print(f'{self.name} съел {food.name}')
            self.alive = True
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    food = Plant

class Predator(Animal):
    food = Plant

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
