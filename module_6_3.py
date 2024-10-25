class Horse:
    x_distance = 0 # пройденный путь
    sound = 'Frrr'

    def run(self, dx): # изменение дистанции Horse
        self.dx = dx
        self.x_distance += self.dx

class Eagle:
    y_distance = 0 # высота полёта
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy): # изменение дистанции Eagle
        self.dy = dy
        self.y_distance += self.dy

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()
print(p1.get_pos())

p1.move(10, 15)
print(p1.get_pos())

p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
