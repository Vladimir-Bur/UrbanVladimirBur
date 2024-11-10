import os
import time

print("Текущая директория:", os.getcwd())
print('')

for root, dirs, files in os.walk('.'):
    for f in files:
        filepath = os.path.join(os.getcwd(), f)
        filetime = os.stat(f).st_ctime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(f).st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {f},\n'
              f'Путь: {filepath},\n'
              f'Размер: {filesize} байт,\n'
              f'Время изменения: {formatted_time},\n'
              f'Родительская директория: {parent_dir}\n')


