import sqlite3

def createTable():

    conn = sqlite3.connect('Library_management.db')

    conn.execute('DROP TABLE IF EXISTS users')

    conn.execute('''
        CREATE TABLE users
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        status INTEGER
        );
    ''')

    conn.execute('DROP TABLE IF EXISTS roles')

    conn.execute('''
        CREATE TABLE roles
        (
        id INTEGER PRIMARY KEY,
        role_name TEXT
        );
    ''')

    conn.execute('DROP TABLE IF EXISTS user_roles')

    conn.execute('''
        CREATE TABLE user_roles
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role_id INTEGER
        );
    ''')

    conn.execute('DROP TABLE IF EXISTS books')
    conn.execute('''
        CREATE TABLE books
        (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_title TEXT,
        book_author TEXT,
        book_language TEXT,
        book_category_id INTEGER,
        book_position TEXT,
        book_pages INTEGER,
        insert_date TEXT,
        cover_image BLOB,
        status TEXT);''')



    conn.execute('DROP TABLE IF EXISTS book_orders ')
    conn.execute('''
        CREATE TABLE book_orders
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        book_id INTEGER,
        borrow_date TEXT,
        return_date TEXT
        );
        ''')

    conn.execute('DROP TABLE IF EXISTS category')
    conn.execute('''
                CREATE TABLE category
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT
                );
            ''')

    conn.commit()
    conn.close()
