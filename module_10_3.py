import threading
import time
from random import randint


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for d in range(1, 101):
            coming_money = randint(50, 500)
            self.balance += coming_money
            print(f'Пополнение: {coming_money}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for t in range(1, 101):
            take_money = randint(50, 500)
            print(f'Запрос на {take_money}')
            if take_money <= self.balance:
                self.balance -= take_money
                print(f'Снятие: {take_money}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
