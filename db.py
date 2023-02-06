import sqlite3

conn = sqlite3.connect('account.db')
def createTable():
    conn.execute('''
    CREATE TABLE account
    ''')