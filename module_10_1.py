import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for x in range(1, word_count + 1):
            file.write(f'Какое-то слово № {x}\n')
            time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {str(file_name)}')
    return f'Запись в файл {str(file_name)} состоялась'

t1 = time.time()
words1 = write_words(10, 'example1.txt')
words2 = write_words(30, 'example2.txt')
words3 = write_words(200, 'example3.txt')
words4 = write_words(100, 'example4.txt')
t2 = time.time()
time_words = round(t2 - t1, 2)
print(f'Время работы функций с аргументами: {time_words} секунд.')

t3 = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
t4 = time.time()
time_thread = round(t4 - t3, 2)
print(f'Время работы потоков: {time_thread} секунд.')
