import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.days = 0

    def battle(self):
        while self.enemy > 0:
            self.enemy -= self.power
            self.days += 1
            time.sleep(1)
            print(f'{self.name} сражается {self.days} день, осталось {self.enemy} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

def current_battles():
    while len(threading.enumerate()) > 1:
        time.sleep(1)
        continue
    print(f'Все битвы закончились!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
time.sleep(1.01)
second_knight.start()

# Вывод строки об окончании сражения
current_battles()
