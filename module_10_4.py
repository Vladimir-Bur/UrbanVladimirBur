import threading
import time
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __str__(self):
        return f'Стол: номер {self.number}'

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(1, 3))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = [*tables]

    def guest_arrival(self, *guests):
        self.guests = [*guests]
        full_table = False
        for guest in self.guests:
            guest.start()
            guest.join()
            if full_table:
                print(f'{guest.name} в очереди')
                self.queue.put(guest.name)
            else:
                counter = len(self.tables)
                for table in self.tables:
                    counter -= 1
                    if table.guest is None:
                        table.guest = guest.name
                        print(f'{table.guest} сел(-а) за стол номер {table.number}')
                        break
                    else:
                        continue

                if counter != 0:
                    continue
                else:
                    full_table = True

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest is not None:
                    time.sleep(randint(2, 5))
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        time.sleep(randint(1, 3))
                        print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    else:
                        continue
            continue

        for table in self.tables:
            if table.guest is not None:
                time.sleep(randint(2, 4))
                print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                table.guest = None
                print(f'Стол номер {table.number} свободен')
            else:
                continue

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

