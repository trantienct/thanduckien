from tkinter import *
from tkinter import messagebox




register = Tk()

username = StringVar()
password = StringVar()
errorUsername = StringVar()
errorPassword = StringVar()
def validate(username, password, role):
    result = {'status': '', 'username': '', 'password': ''}
    if username == '':
        result['status'] = False
        if result['username'] == '':
            result['username'] = 'You must type username'
        # return result
    if len(username) < 3 or len(username) > 10:
        result['status'] = False
        if result['username'] == '':
            result['username'] = 'Username must greater than 3 or less than 10'
    if  password == '':
        result['status'] = False
        if result['password'] == '':
            result['password'] = 'You must type password'
    if len(password) < 3 or len(password) > 10:
        result['status'] = False
        if result['password'] == '':
            result['password'] = 'Password must greater than 3 or less than 10'
    return result
def check():
    txtuser = username.get()
    txtpass = password.get()
    result = validate(txtuser, txtpass, '')
    if result['status'] == False:
        errorUsername.set(result['username'])
        errorPassword.set(result['password'])
    else:
        errorUsername.set('')
        errorPassword.set('')
        #check DB


register.title('Login')
register.geometry('400x400')
lblAccount = Label(register, text='Account')
lblAccount.grid(row=0, column=0)
txtAcount = Entry(register, textvariable=username)
txtAcount.grid(row=0, column=1)
lblAccountError = Label(register, text='', textvariable=errorUsername)
lblAccountError.grid(row=1, column=1)
lblPassword = Label(register, text='Password')
lblPassword.grid(row=2, column=0, padx=10)
txtPassword = Entry(register, show='*', textvariable=password)
txtPassword.grid(row=2, column=1, padx=10)
lblPassError = Label(register, text='', textvariable=errorPassword)
lblPassError.grid(row=3, column=1)
lblRePassword = Label(register, text='Retype Password')
lblRePassword.grid(row=4, column=0, padx=10)
txtRePassword = Entry(register, show='*')
txtRePassword.grid(row=4, column=1, padx=10)
btnRegister = Button(register, text='Register', command=check)
btnRegister.grid(row=5, column=0)
register.mainloop()
