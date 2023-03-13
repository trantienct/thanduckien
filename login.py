from tkinter import *
from tkinter import messagebox
from DB import *
from adminDashboard import *
from studentDashboard import *
from lib import *
conn = sqlite3.connect('Library_management.db')

def loginPage(root):
    def login():
        if account.get() == '' or password.get() == '':
            messagebox.showinfo('Error', 'Username and Password is not empty')
        else:
            cur = conn.execute('SELECT * FROM users WHERE username =? and password =?', (account.get(), password.get(),))
            row = cur.fetchone()
            print(row)
            if row is None:
                messagebox.showinfo("Account Not Found", "This account is not exist")
            else:
                if row[3] == 1:
                    role = getRole(conn, account.get())
                    if role[0] == 'Administrator':
                        root.withdraw()
                        adminDashboard(root, account.get())
                    elif role[0] == 'Student':
                        root.withdraw()
                        studentDashboard()
                else:
                    messagebox.showinfo('Error', 'Your account is inactive')

    def reset():
        account.set('')
        password.set('')
    def register():
        def executeRegister():
            registerName = txtAcount.get()
            registerPass = txtPassword.get()
            registerRetypePass = txtRePassword.get()
            status = '1'
            if registerName == '' or registerPass == '':
                messagebox.showinfo('Error', 'Username and Password is not empty')
            else:
                cur = conn.execute('SELECT * FROM users WHERE username =?', (registerName,))
                row = cur.fetchall()
                if len(row) > 0:
                    messagebox.showinfo('Error', 'Username is exist')
                else:
                    print('A')
                    if registerPass != registerRetypePass:
                        messagebox.showinfo('Error', 'Password and Password Retype is mismatch')
                    else:
                        # insert to DB
                        cur1 = conn.execute('INSERT INTO users (username,password, status) VALUES (?,?,?)',
                                            (registerName, registerPass, status))
                        user_id = cur1.lastrowid
                        role_id = 2
                        cur2 = conn.execute('INSERT INTO user_roles(user_id, role_id) VALUES(?,?)', (user_id, role_id))
                        conn.commit()
                        print('Register successfully')
                        register.destroy()
                        root.deiconify()

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
        btnRegister = Button(register, text='Register', command=executeRegister)
        btnRegister.grid(row=3, column=0)

    account = StringVar()
    password = StringVar()
    lblHeading = Label(root, text='Login Page', font='Arial 20')
    lblHeading.grid(row=0, column=0, columnspan=2, sticky='we', padx=10, pady=10)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    lblAccount = Label(root, text='Your Account', font='Arial 12')
    lblAccount.grid(row=1, column=0, pady=5)
    txtAccount = Entry(root, font='Arial 16', textvariable=account)
    txtAccount.grid(row=1, column=1, pady=5)

    lblPassword = Label(root, text='Your Password', font='Arial 12')
    lblPassword.grid(row=2, column=0, pady=5)
    txtPassword = Entry(root, font='Arial 16', textvariable=password, show='*')
    txtPassword.grid(row=2, column=1, pady=5)

    btnCancel = Button(root, text='Cancel', font='Arial 10', width=10)
    btnCancel.grid(row=3, column=0)

    btnLogin = Button(root, text='Login', font='Arial 10', command=login, width=10)
    btnLogin.grid(row=3, column=1)

    btnRegister = Button(root, text='Register', command=register, width=10)
    btnRegister.grid(row=4, column=0, columnspan=2)
