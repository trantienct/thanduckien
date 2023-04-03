import sqlite3
from tkinter import messagebox
conn = sqlite3.connect('Library_management.db')
def getRole(conn, username):
    query = conn.execute('''
                          SELECT roles.role_name FROM roles
                          LEFT JOIN user_roles ON user_roles.role_id = roles.id
                          LEFT JOIN users ON user_roles.user_id = users.id
                          WHERE users.username =?
                          ''', (username,))
    result = query.fetchone()
    return result
def getRoleLists(conn):
    query = conn.execute('''
        SELECT role_name FROM roles
    ''')
    result = query.fetchall()
    final_result = [i[0] for i in result]
    return final_result

def addNewUser(conn, userName, password, role_id):
    checkUsser = conn.execute('''
        SELECT * FROM users WHERE username =?''',(userName,))
    result = checkUsser.fetchall()
    if len(result) == 0:
        cur1 = conn.execute('INSERT INTO users (username, password, status) VALUES(?,?,?)', (userName, password, 1))
        user_id = cur1.lastrowid
        cur2 = conn.execute('INSERT INTO user_roles(user_id, role_id) VALUES(?,?)', (user_id, role_id))
        conn.commit()
        return True

    else:
        return False

def validateData(username, password):
    result = {'status': '', 'username': '', 'password': ''}
    if username == '':
        result['status'] = False
        if result['username'] == '':
            result['username'] = 'You must type username'
    if len(username) < 3 or len(username) > 30:
        result['status'] = False
        if result['username'] == '':
            result['username'] = 'Username must greater than 3 or less than 10'
    if username.count('@') >0 or username.count('%') >0 or username.count('$') >0 or username.count('#') >0:
        result['status'] = False
        if result['username'] == '':
            result['username'] = "Username mustn't have symbols like '@,!,%,$'"


    if password == '':
        result['status'] = False
        if result['password'] == '':
            result['password'] = 'You must type password'
        return result

    if len(password) < 8 or len(password) > 30:
        result['status'] = False
        if result['password'] == '':
            result['password'] = 'Password must greater than 8 or less than 30'
        return result
    if password.count('@') <1 or password.count('%') < 1  or password.count('$') <1 or password.coun('#') <1:
        result['status'] = False
        if result['password'] == '':
            result['password'] = "Password must have symbols like '@,!,%,$'"

    return result





