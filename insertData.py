import sqlite3
from DB import *
createTable()
conn = sqlite3.connect('Library_management.db')
user_lists = [('admin', '123456789', 1), ('student', '123456789',1)]
role_lists = [(1, 'Administrator'), (2, 'Student')]
category_lists = [('Math'), ('Literature'), ('English')]
user_role_lists = [(1,1), (2,2)]


for user in user_lists:
    conn.execute('INSERT INTO users (username, password, status) VALUES (?,?,?)', (user[0], user[1], user[2]))
    conn.commit()
for role in role_lists:
    conn.execute('INSERT INTO roles (id, role_name) VALUES(?,?)', (role[0], role[1]))
    conn.commit()
for user_role in user_role_lists:
    conn.execute('INSERT INTO user_roles (user_id, role_id) VALUES (?,?)', (user_role[0], user_role[1]))
    conn.commit()
for category in category_lists:
    conn.execute('INSERT INTO category (category_name) VALUES(?)', (category[1]))
    conn.commit()
conn.close()

