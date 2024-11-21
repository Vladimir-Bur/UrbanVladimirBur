def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        prime_number = True
        for i in [2, 3, 5, 7]:
            if number == 3 or number == 5 or number ==7:
                break
            if number % i != 0:
                continue
            else:
                prime_number = False
                break
        if number == 0:
            print('Ноль - это особенное число!')
        elif prime_number:
            print('Простое')
        elif not prime_number:
            print('Составное')
        return number
    return wrapper


@is_prime
def sum_three(*args):
    return sum(list(args))

result = sum_three(2, 3, 6)
print(result)
