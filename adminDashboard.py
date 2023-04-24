from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from lib import *
conn = sqlite3.connect('Library_management.db')
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

    def viewUserList():
        user_list = Toplevel(root)
        user_list.title('View user list')
        user_list.geometry('600x400')
        columns = ('id', 'username', 'role')
        view_user = ttk.Treeview(user_list, columns=columns,show='headings')
        view_user.heading('id', text='ID')
        view_user.heading('username', text='Username')
        view_user.heading('role', text='Role')
        view_user.grid(column=0,row=0,sticky='nsew')
        cur = conn.execute('''SELECT users.id, users.username, roles.role_name 
                           FROM users
                           LEFT JOIN user_roles ON users.id = user_roles.user_id
                           LEFT JOIN roles ON user_roles.role_id = roles.id
                           WHERE roles.id = 2 ''')
        row = cur.fetchall()
        for i in row:
            view_user.insert('', END, values=(i[0], i[1], i[2]))

    def addUser():
        error_username = StringVar()
        error_password = StringVar()
        add_user = Toplevel(root)
        add_user.geometry('400x400')
        add_user.title('Add new user')
        lblAccount = Label(add_user, text='Account',font =15)
        lblAccount.grid(row=0, column=0, padx=15)
        txtAcount = Entry(add_user, font=15)
        txtAcount.grid(row=0, column=1)
        lblerrorAccount = Label(add_user, textvariable=error_username)
        lblerrorAccount.grid(row=1, column=1)
        lblPassword = Label(add_user, text='Password',font=15)
        lblPassword.grid(row=2, column=0, padx=15)
        txtPassword = Entry(add_user, show='*', font=15)
        txtPassword.grid(row=2, column=1, padx=10, pady=5)
        lblerrorPassword = Label(add_user, textvariable=error_password )
        lblerrorPassword.grid(row=3, column=1)
        lblRole = Label(add_user, text = 'Role:', font=15)
        lblRole.grid(row=4, column=0, padx=15)
        ComboRole = ttk.Combobox(add_user, font='Arial 16')
        ComboRole['values'] = getRoleLists(conn)
        ComboRole.grid(row=4, column=1, pady=5)

        def executeAdd():
            registerName = txtAcount.get()
            registerPass = txtPassword.get()
            role = ComboRole.get()
            cur2 = conn.execute('SELECT id FROM roles WHERE role_name =?', (role,))
            role_id = cur2.fetchone()
            print(registerName)
            check_user = validateUser(registerName,registerPass)
            if check_user['status'] == False:
                error_username.set(check_user['username'])
                error_password.set(check_user['password'])
            else:
                error_password.set('')
                error_username.set('')
                new_user = addNewUser(conn, registerName, registerPass, role_id[0])
        btnAdd = Button(add_user, text='Create', command=executeAdd)
        btnAdd.grid(row=5, column=0)
        btnBack = Button(add_user, text ='Back')
        btnBack.grid(row=5, column=1)


    def editUser():
        def loadTable(treeView,data):
            treeView.delete(*treeView.get_children())
            for i in data:
                treeView.insert('', END, values=(i[0], i[1], i[2]))
        def userInfo(event):
            name = StringVar()
            role = StringVar()
            index = edit_user.focus()
            selectValue = edit_user.item(index)
            studentData = selectValue['values']
            name.set(studentData[1])
            role.set(studentData[2])

            Info = Toplevel(root)
            Info.title('User Info')
            Info.geometry('400x400')
            Info.columnconfigure(1, weight=1)
            Info.columnconfigure(2, weight=1)
            Info.columnconfigure(3, weight=1)
            lblUsername = Label(Info, text='Username:', font='Arial 12')
            lblUsername.grid(row=1, column=0, pady=5)
            txtUsername = Entry(Info, font='Arial 16', textvariable=name)
            txtUsername.grid(row=1, column=1, pady=5)

            lblRole = Label(Info, text='Role: ', font='Arial 12')
            lblRole.grid(row=2, column=0, pady=5)
            ComboRole = ttk.Combobox(Info, font='Arial 16', textvariable=role)
            ComboRole['values'] = getRoleLists(conn)
            ComboRole.grid(row=3, column=0, pady=5)
            def setData():
                user_id = studentData[0]
                new_username = txtUsername.get()
                new_role = ComboRole.get()
                conn.execute('UPDATE users SET username = ? WHERE id = ?', (new_username, user_id))
                cur2 = conn.execute('SELECT id FROM roles WHERE role_name =?', (new_role,))
                role_id = cur2.fetchone()
                conn.execute('UPDATE user_roles SET role_id= ? WHERE user_id= ? ', (role_id[0], user_id))
                conn.commit()
                cur3 = conn.execute('''
                            SELECT users.id,users.username, roles.role_name FROM users
                            LEFT JOIN user_roles ON users.id = user_roles.user_id
                            LEFT JOIN roles ON user_roles.role_id = roles.id
                             ''')
                result = cur3.fetchall()
                loadTable(edit_user, result)
                Info.destroy()

            btnUpdate = Button(Info, text = 'Update', command=setData)
            btnUpdate.grid(row = 4, column=0, pady=5)
            Info.mainloop()


        edit = Toplevel(root)
        edit.title('View user list')
        edit.geometry('400x400')
        columns = ('id', 'username', 'role')
        edit_user = ttk.Treeview(edit, columns=columns, show='headings')
        edit_user.heading('id', text='ID')
        edit_user.heading('username', text='Username')
        edit_user.heading('role', text='Role')
        edit_user.grid(column=0, row=0, sticky='nsew')
        edit_user.bind("<ButtonRelease-1>",userInfo)
        cur = conn.execute('''SELECT users.id, users.username, roles.role_name 
                           FROM users
                           LEFT JOIN user_roles ON users.id = user_roles.user_id
                           LEFT JOIN roles ON user_roles.role_id = roles.id
                           ORDER BY users.id ASC ''')

        row = cur.fetchall()
        for i in row:
            edit_user.insert('',END,values=(i[0], i[1], i[2]))

    def addBook():
        addBook = Toplevel(root)
        addBook.geometry('600x600')
        cur = conn.execute('SELECT category_name FROM category')
        category = cur.fetchall()
        title = StringVar()
        author = StringVar()
        category_name = StringVar()
        languagues = StringVar()
        pages = IntVar()
        insert_date = StringVar()
        position = StringVar()
        error_title = StringVar()
        error_author = StringVar()
        error_category = StringVar()
        error_languagues = StringVar()
        error_insertdate = StringVar()
        addBook.title('Add New Book')
        lblHeading = Label(addBook, text='Add new book', font='Arial 20')
        lblHeading.grid(row=0, column=0, columnspan=2, sticky='we', padx=10, pady=10)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.columnconfigure(4, weight=1)
        root.columnconfigure(5, weight=1)
        root.columnconfigure(6, weight=1)
        lblTitle = Label(addBook, text='Title', font='Arial 12')
        lblTitle.grid(row=1, column=0, pady=5)
        txtTitle = Entry(addBook, font='Arial 16', textvariable=title)
        txtTitle.grid(row=1, column=1, pady=5)
        errorTitle = Label(addBook, textvariable=error_title)
        errorTitle.grid(row =2, column=1)

        lblAuthor = Label(addBook, text='Author', font='Arial 12')
        lblAuthor.grid(row=3, column=0, pady=5)
        txtAuthor = Entry(addBook, font='Arial 16', textvariable=author)
        txtAuthor.grid(row=3, column=1, pady=5)
        errorAuthor = Label(addBook, textvariable=error_author)
        errorAuthor.grid(row=4, column=1)

        lblCategory = Label(addBook, text='Category', font='Arial 12')
        lblCategory.grid(row=5, column=0, pady=5)
        txtCategory = ttk.Combobox(addBook, font='Arial 14', textvariable=category_name)
        txtCategory['values'] = (category)
        txtCategory.grid(row=5, column=1, pady=5)
        errorCategory = Label(addBook, textvariable=error_category)
        errorCategory.grid(row=6, column=1)

        lblLanguague = Label(addBook, text='Languages', font='Arial 12')
        lblLanguague.grid(row=7, column=0, pady=5)
        txtLanguague = ttk.Combobox(addBook, font='Arial 14', textvariable=languagues)
        txtLanguague['values'] = ('Vietnamese', 'English', 'French')
        txtLanguague.grid(row=7, column=1, pady=5)
        errorLanguages = Label(addBook, textvariable=error_languagues)
        errorLanguages.grid(row=8, column=1)

        lblPage = Label(addBook, text='Page', font='Arial 12')
        lblPage.grid(row=9, column=0, pady=5)
        txtPage = Entry(addBook, font='Arial 16', textvariable=pages)
        txtPage.grid(row=9, column=1, pady=5)

        lblInsertDate = Label(addBook, text='Insert Date', font='Arial 12')
        lblInsertDate.grid(row=11, column=0, pady=5)
        txtInsertDate = Entry(addBook, font='Arial 16', textvariable=insert_date)
        txtInsertDate.grid(row=11, column=1, pady=5)
        errorInsert_date = Label(addBook, textvariable=error_insertdate)
        errorInsert_date.grid(row=12, column=1)

        lblPosition = Label(addBook, text='Position', font='Arial 12')
        lblPosition.grid(row=13, column=0, pady=5)
        txtPosition = Entry(addBook, font='Arial 16', textvariable=position)
        txtPosition.grid(row=13, column=1, pady=5)
        def executeAddBook():
            book_title = title.get()
            book_author = author.get()
            book_category = category_name.get()
            book_languagues = languagues.get()
            book_pages = pages.get()
            book_insert_date = insert_date.get()
            book_position = position.get()
            cur = conn.execute('SELECT id FROM category WHERE category_name = ?',(book_category,))
            book_category_id = cur.fetchone()
            print(book_author)
            check = validateBook(book_title, book_author,book_category,book_languagues, book_insert_date)
            print(check)
            if check['status'] == True:
                add_data = conn.execute('INSERT INTO books (book_title, book_author, book_language, book_category_id, book_position, book_pages, insert_date) VALUES(?,?,?,?,?,?)',(book_title, book_author, book_languagues, book_category_id, book_position, book_pages, insert_date))
                messagebox.showinfo('Add book', 'Add book successfully')
                addBook.withdraw()
                conn.commit()

            else:
                error_title.set(check['title'])
                error_author.set(check['author'])
                error_category.set(check['category'])
                error_languagues.set(check['languages'])
                error_insertdate.set(check['insert_date'])





        btn_add_book = Button(addBook, text='Add', font='Arial 10', width=15, command=executeAddBook)
        btn_add_book.grid(row=15, column=1, columnspan=2, sticky='we')
    admin = Toplevel(root)
    admin.columnconfigure(0, weight=1)
    admin.columnconfigure(1, weight=1)
    admin.title('Admin Dashboard')
    admin.geometry('400x400')
    lblText = Label(admin, text='Hello, ' + user_name, font='Arial 14')
    lblText.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lblUserManagement = Label(admin, text='User Management ', font='Arial 12')
    lblUserManagement.grid(row=1, column=0, padx=10)
    btnViewUserList = Button(admin, text='View User List ', font='Arial 12', command=viewUserList)
    btnViewUserList.grid(row=2, column=0, padx=10)
    btnUpdate_User = Button(admin, text='Update User ', font='Arial 12',command=editUser)
    btnUpdate_User.grid(row=3, column=0, padx=10)
    btnDelete_User = Button(admin, text='Delete User ', font='Arial 12')
    btnDelete_User.grid(row=4, column=0, padx=10)
    btnAdd_User = Button(admin, text='Add user ', font='Arial 12', command = addUser)
    btnAdd_User.grid(row=5, column=0, padx=10)


    lblBookManagement = Label(admin, text='Book Management ', font='Arial 12')
    lblBookManagement.grid(row=1, column=1, padx=10)
    btnAddBook = Button(admin, text='Add a book', font='Arial 12', command=addBook)
    btnAddBook.grid(row=2, column=1, padx=10)
    admin.mainloop()