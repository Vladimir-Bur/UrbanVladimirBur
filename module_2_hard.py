hello = 99
while hello != 0:
    print(' *** Добро пожаловать в программу "Пароль"! ***')
    print('*** Для выхода из программы введите: 0 (ноль) ***')
    print(" ")
    num = int(input("Введите любое число от 3 до 20: "))
    if 3 <= num <= 20:
        def psw():
            result = []
            for j in range(int(num / 2 + 1)):
                for k in range(int(num)):
                    if sum([int(j + 1), int(k + 2)]) <= num and int(j + 1) < int(k + 2):
                        if num % sum([int(j + 1), int(k + 2)]) == 0:
                            result.append([int(j + 1), int(k + 2)])
            new_result = []
            for p in range(len(result)):
                new_result.append(result[p][0])
                new_result.append(result[p][1])
            new_result = str(new_result)
            new_result = new_result.replace(" ", "")
            new_result = new_result.replace("[", "")
            new_result = new_result.replace("]", "")
            new_result = new_result.replace(",", "")
            return new_result

        print("Для числа:", num)
        print("Пароль:" ,psw())
        print(" ")
        continue
    elif num == 0:
        hello = num
    else:
        print("!!! Вы ввели неверное число, попробйте снова !!!")
        print(" ")
        del num
    continue