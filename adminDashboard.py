from tkinter import *

# User Management
## View User List
## Update User: Role, status
## Delete user
# Book Management
## Book list
## Add, Edit and Delete Book
## Search Book
## View Book order: Borrow, return.



def adminDashboard(root, user_name):
    admin = Toplevel(root)
    admin.columnconfigure(0, weight=1)
    admin.columnconfigure(1, weight=1)
    admin.title('Admin Dashboard')
    admin.geometry('400x400')
    lblText = Label(admin, text='Hello, ' + user_name, font='Arial 14')
    lblText.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lblUserManagement = Label(admin, text='User Management ', font='Arial 12')
    lblUserManagement.grid(row=1, column=0, padx=10)
    lblBookManagement = Label(admin, text='Book Management ', font='Arial 12')
    lblBookManagement.grid(row=1, column=1, padx=10)
    admin.mainloop()