import sqlite3
conn = sqlite3.connect('Library_management.db')

cur = conn.execute('SELECT * FROM users')
row = cur.fetchall()
cur1 = conn.execute('SELECT * FROM user_roles')
row1 = cur1.fetchall()
print(row1)
print(row)