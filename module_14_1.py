import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

#for i in range(1, 11):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                   (f'User{i}',f'example{i}@gmail.com', f'{i * 10}', '1000'))

#n = 1
#for b in range(5):
#    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{n}'))
#    n += 2

#User_Del = 1
#for d in range(4):
#    cursor.execute('DELETE FROM Users WHERE id = ?', (f'{User_Del}',))
#    User_Del += 3

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
