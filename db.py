import sqlite3

conn = sqlite3.connect('account.db')


def createTable():
    conn.execute('DROP TABLE IF EXISTS account')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS account
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name TEXT,
        balance FLOAT
        );
    ''')
    conn.execute('DROP TABLE IF EXISTS history')
    conn.execute('''
            CREATE TABLE IF NOT EXISTS history
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            htype TEXT,
            money FLOAT
            );
        ''')

    conn.commit()

createTable()