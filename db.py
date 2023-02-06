import sqlite3

conn = sqlite3.connect('account.db')
conn.execute('DROP TABLE IF EXISTS account')
def createTable():
    conn.execute('''
        CREATE TABLE IF NOT EXISTS account
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name TEXT,
        balance FLOAT
        );
    ''')
    conn.commit()

