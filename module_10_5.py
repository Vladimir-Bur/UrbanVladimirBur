import time
from multiprocessing import Pool


def read_info(names):
    if type(names) is str:
        names = [names]
    all_data = []
    for name in names:
        with open(name, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                all_data.append(f'{line}\n')
                if not line:
                    break
        file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

"""# Линейный вызов
t1 = time.time()
read_info(filenames)
t2 = time.time()
print(t2 - t1)"""

# Многопроцессный
if __name__ == '__main__':
    t3 = time.time()
    with Pool(4) as pool:
        res = pool.map(read_info, filenames)
    t4 = time.time()
    print(t4 - t3)
