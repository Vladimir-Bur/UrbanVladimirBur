import sqlite3

connection = sqlite3.connect('database_14_5.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL, 
        description TEXT,
        price INTEGER NOT NULL)
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL)
        ''')
    connection.commit()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}',f'{email}', f'{age}', '1000'))
    connection.commit()

def is_included(username):
    usernames = cursor.execute('SELECT username FROM Users').fetchall()
    usm_list = [str(i[0]) for i in usernames]
    if username in usm_list:
        return True
    else:
        return False

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products


def set_products():
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'Product{i}',f'описание{i}', (i * 100)))
    connection.commit()

#initiate_db()
#set_products()
