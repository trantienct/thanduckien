import sqlite3

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