import sqlite3
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
    result = checkUsser.fetchone()
    print(result)
    if len(result) == 0:
        cur1 = conn.execute('INSERT INTO users (username, password, status) VALUES(?,?,?)', (userName, password, 1))
        user_id = cur1.lastrowid
        cur2 = conn.execute('INSERT INTO user_roles(user_id, role_id) VALUES(?,?)', (user_id, role_id))
        conn.commit()
        return True

    else:
        return False



