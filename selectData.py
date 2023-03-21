import sqlite3
from lib import *
conn = sqlite3.connect('Library_management.db')

cur = conn.execute('SELECT * FROM users')
row = cur.fetchall()
cur1 = conn.execute('SELECT * FROM user_roles')
row1 = cur1.fetchall()
#
# cur2 = conn.execute('SELECT * FROM roles')
# row2 = cur2.fetchall()
# print(row1)
# print(row)
# print(row2)
# role_name = getRoleLists(conn)
# final_role = [i[0] for i in role_name]
# print(final_role)