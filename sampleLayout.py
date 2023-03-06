from tkinter import *

def loginPage(root):
    acount = StringVar()
    password = StringVar()
    lblHeading = Label(root, text='Login Page', font='Arial 20')
    lblHeading.grid(row=0, column=0, columnspan=2, sticky='we', padx=10, pady=10)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    lblAccount = Label(root, text='Your Account', font='Arial 12')
    lblAccount.grid(row=1, column=0, pady=5)
    txtAccount = Entry(root, font='Arial 16')
    txtAccount.grid(row=1, column=1, pady=5)

    lblPassword = Label(root, text='Your Password', font='Arial 12')
    lblPassword.grid(row=2, column=0, pady=5)
    txtPassword = Entry(root, font='Arial 16')
    txtPassword.grid(row=2, column=1, pady=5)

    btnCancel = Button(root, text='Cancel', font='Arial 10', width=10)
    btnCancel.grid(row=3, column=0)

    btnLogin = Button(root, text='Login', font='Arial 10', width=10)
    btnLogin.grid(row=3, column=1)