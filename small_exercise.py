from tkinter import *
from tkinter import messagebox

register = Tk()
register.title('Login')
register.geometry('400x400')
lblAccount = Label(register, text='Account')
lblAccount.grid(row=0, column=0)
txtAcount = Entry(register)
txtAcount.grid(row=0, column=1)
lblAccountError = Label(register, text='Your username must not be empty')
lblAccountError.grid(row=1, column=1)
lblPassword = Label(register, text='Password')
lblPassword.grid(row=2, column=0, padx=10)
txtPassword = Entry(register, show='*')
txtPassword.grid(row=2, column=1, padx=10)
lblPassError = Label(register, text='Your password must not be empty')
lblPassError.grid(row=3, column=1)
lblRePassword = Label(register, text='Retype Password')
lblRePassword.grid(row=4, column=0, padx=10)
txtRePassword = Entry(register, show='*')
txtRePassword.grid(row=4, column=1, padx=10)
btnRegister = Button(register, text='Register')
btnRegister.grid(row=5, column=0)
register.mainloop()
def validate(username, password, role):
    result = {'status': '', 'message': ''}
    if username == '' or password == '':
        result['status'] = False
        result['message'] = 'You must type username or password'
        return result
    if len(username) < 3 or len(username) > 10:
        result['status'] = False
        result['message'] = 'Username must greater than 3 or less than 10'
        return result
    if len(password) < 3 or len(password) > 10:
        result['status'] = False
        result['message'] = 'Password must greater than 3 or less than 10'
        return result
    return result

username = '12345'
password = '12345'
role = ''
check = validate(username, password, role)

if check['status'] == False:
    print(check['message'])