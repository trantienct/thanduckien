from tkinter import *

def loginPage(root):
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

    btnCancel = Button(root, text='Cancel')
    btnCancel.grid(row=2, column=0, )
    btnLogin = Button(root, text='Login')
    btnLogin.grid(row=2, column=1)

    btnRegister = Button(root, text='Register')
    btnRegister.grid(row=3, column=0, columnspan=2)