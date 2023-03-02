from tkinter import *
from tkinter import messagebox

def loginPage(root):
    def login():
        messagebox.showinfo('Login', f'user name: {acount.get()}, password: {password.get()}')

    def reset():
        acount.set('')
        password.set('')

    def register():
        register = Toplevel(root)
        lblAccount = Label(register, text='Account')
        lblAccount.grid(row=0, column=0)
        txtAcount = Entry(register)
        txtAcount.grid(row=0, column=1)
        lblPassword = Label(register, text='Password')
        lblPassword.grid(row=1, column=0, padx=10)
        txtPassword = Entry(register, show='*')
        txtPassword.grid(row=1, column=1, padx=10)
        lblRePassword = Label(register, text='Retype Password')
        lblRePassword.grid(row=2, column=0, padx=10)
        txtRePassword = Entry(register, show='*')
        txtRePassword.grid(row=2, column=1, padx=10)
        btnRegister = Button(register, text='Register')
        btnRegister.grid(row=3, column=0)
    acount = StringVar()
    password = StringVar()
    lblAccount = Label(root, text='Account')
    lblAccount.grid(row=0, column=0)
    txtAcount = Entry(root, textvariable=acount)
    txtAcount.grid(row=0, column=1)
    lblPassword = Label(root, text='Password')
    lblPassword.grid(row=1, column=0, padx=10)
    txtPassword = Entry(root, textvariable=password, show='*')
    txtPassword.grid(row=1, column=1, padx=10)

    btnCancel = Button(root, text='Cancel', command=reset)
    btnCancel.grid(row=2, column=0 )
    btnLogin = Button(root, text='Login', command=login)
    btnLogin.grid(row=2, column=1)

    btnRegister = Button(root, text='Register', command=register)
    btnRegister.grid(row=3, column=0, columnspan=2)
