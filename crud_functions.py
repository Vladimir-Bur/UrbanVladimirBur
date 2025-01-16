import sqlite3

connection = sqlite3.connect('database_products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL, 
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    return all_products

#initiate_db()
#for i in range(1, 5):
#    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#                   (f'Product{i}',f'описание{i}', (i * 100)))
