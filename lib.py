import sqlite3
from tkinter import messagebox
import re
from datetime import datetime
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

def validateUser(username, password):
    result = {'status': '', 'username': '', 'password': ''}
    check_password = re.search('[0-9][A-Z][!@#$%^&*()+]', password)
    check_username = re.search('[A-Z][a-z]', username)

    result['status'] = True
    if check_password is None:
        result['password'] = 'Your password must be more special'
        result['status'] = False

    if check_username is None:
        result['username'] = 'Your username must be more special'
        result['status'] = False
    return result

def validateBook(title, author, category, languages, insert_date):
    result = {'status': '', 'title': '', 'author': '', 'category':'', 'languages':'', 'insert_date':''}
    current_time = datetime.now().date()
    insert_date_format = datetime.strptime(insert_date, '%d/%m/$Y').date()
    if len(title) >= 50:
        result['title'] = "Your title can't be more than 50 charaters"
        result['status'] = False
    check_author = re.search('[A-Z][a-z]', author)
    check_category = re.search('[A-Z][a-z]', category)
    check_languages = re.search('[A-Z][a-z]', languages)
    result['status'] = True
    if check_author is None:
        result['author'] = "Author's name can't be null"
        result['status'] = False

    if check_category is None:
        result['category'] = "Category can't be null"
        result['status'] = False

    if check_languages is None:
        result['languages'] = "languages can't be null"
        result['status'] = False
    if insert_date_format > current_time:
        result['insert_date'] = ["Your insert date can't be bigger than current date"]
        result['status'] = False













