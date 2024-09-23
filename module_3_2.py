def send_email(text, recipient, sender='university.help@gmail.com'):
    if '@' not in recipient:
        print(' ')
        print('Невозможно отправить письмо на адрес:', recipient)
    elif ('.com' not in recipient
                and '.ru' not in recipient
                and '.net' not in recipient):
        print(' ')
        print('Невозможно отправить письмо на адрес:', recipient)
    elif '@' not in sender:
        print(' ')
        print('Невозможно отправить письмо с адреса:', sender)
    elif ('.com' not in sender
                and '.ru' not in sender
                and '.net' not in sender):
        print(' ')
        print('Невозможно отправить письмо с адреса:', sender)
    elif recipient == sender:
        print(' ')
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print(' ')
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!',
              'Письмо успешно отправлено с адреса:', sender, 'на адрес:', recipient)
        print('Текст письма:', text)
    else:
        print(' ')
        print('Письмо успешно отправлено с адреса:', sender, 'на адрес:', recipient)
        print('Текст письма:', text)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
