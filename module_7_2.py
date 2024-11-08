import io

def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings = info
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    number_strings = 0
    for t in strings:
        number_strings += 1
        start_text = file.tell()
        file.write(f'{t} \n')
        text_strings = f'{t}'
        strings_positions[(number_strings, start_text)] = text_strings
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

