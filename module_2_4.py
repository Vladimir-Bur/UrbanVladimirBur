numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in numbers:
    for j in numbers[:(i-1)]:
        if i != 1 and i == 2:
            Primes.append(i)
        elif i != 1 and j != 1 and i % j == 0 and i not in Not_Primes:
            Not_Primes.append(i)
        elif i in Primes:
            Primes.remove(i)
        elif j != 1 and i % j != 0 and i not in Primes and i not in Not_Primes:
            Primes.append(i)
print(Primes)
print(Not_Primes)
