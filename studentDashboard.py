import io
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from lib import *
from PIL import ImageTk, Image
from tkinter import filedialog
conn = sqlite3.connect('Library_management.db')

def studentDashboard(root, username, password):
    def updateInfo():
        user_info = Toplevel(root)
        user_info.title('User Info')
        user_info.geometry('600x400')
        stored_username = StringVar()
        stored_password = StringVar()
        stored_username.set(username)
        stored_password.set(password)
        lblUsername = Label(user_info, text='Username')
        lblUsername.grid(column=0, row=0, sticky='w')
        entryUsername = Entry(user_info, textvariable=stored_username)
        entryUsername.grid(column=1, row=0)
        lblPassword = Label(user_info, text='Password:')
        lblPassword.grid(column=0, row=1, sticky='w')
        entryPassword = Entry(user_info, textvariable=stored_password)
        entryPassword.grid(column=1, row=1)
        btnUpdate = Button(user_info, text = 'Update')
        btnUpdate.grid(column=0, row=2, columnspan=2)
        user_info.mainloop()

    def viewBookList():
        def bookInfo(event):
            index = view_book.focus()
            selectValue = view_book.item(index)
            bookData = selectValue['values']
            Info = Toplevel(root)
            Info.title('book Info')
            Info.geometry('600x400')
            Title = Label(Info, text=f'Title: {bookData[1]}', font=20)
            Title.grid(column=0, row=0, sticky='w', pady=10)
            Author = Label(Info, text=f'Author: {bookData[2]}', font=20)
            Author.grid(column=0, row=1, sticky='w')
            Category = Label(Info, text=f'Category: {bookData[3]}', font=20)
            Category.grid(column=0, row=2, sticky='w', pady=10)
            Language = Label(Info, text=f'Language: {bookData[4]}', font=20)
            Language.grid(column=0, row=3, sticky='w', pady=10)
            Return_date = Label(Info, text='Return data:', font=20)
            Return_date.grid(column=0, row = 4, sticky='w', pady=10)
            txtReturn_date = Entry(Info)
            txtReturn_date.grid(column=1, row = 4, pady=10)
            btnBorrow_book = Button(Info, text='Borrow book')
            btnBorrow_book.grid(column=0, row = 5, columnspan=2, pady=10)
            lblImage = Label(Info, width=100, height=100)
            lblImage.grid(column=1, row=0, columnspan=2, rowspan=4)
            cur = conn.execute('SELECT cover_image FROM books WHERE book_id = ?', (bookData[0],))
            row = cur.fetchone()
            image = row[0]
            cover_image = Image.open(io.BytesIO(image))
            resize_image = cover_image.resize((100, 100))
            image_from_db = ImageTk.PhotoImage(resize_image)
            lblImage.config(image=image_from_db)
            lblImage.image = image_from_db

        book_list = Toplevel(root)
        book_list.title('View book list')
        book_list.geometry('1200x800')
        columns = ('id', 'title', 'author', 'category', 'language', 'status')
        view_book = ttk.Treeview(book_list, columns=columns, show='headings')
        view_book.heading('id', text='ID')
        view_book.heading('title', text='Title')
        view_book.heading('author', text='Author')
        view_book.heading('category', text='Category')
        view_book.heading('language', text='Language')
        view_book.heading('status', text='Status')
        view_book.grid(column=0, row=0, sticky='nsew')
        cur = conn.execute('''SELECT books.book_id, books.book_title, books.book_author, books.book_language, category.category_name, books.status  
                                      FROM books
                                      LEFT JOIN category ON book_category_id = category.id
                                      WHERE books.status = "open" ''')
        row = cur.fetchall()
        for i in row:
            view_book.insert('', END, values=(i[0], i[1], i[2], i[4], i[3], i[5]))
        view_book.bind("<ButtonRelease-1>", bookInfo)

    student = Toplevel(root)
    student.title('Student Dashboard')
    student.geometry('400x400')
    lblText = Label(student, text='Student', font='Arial 14')
    lblText.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lblUserManagement = Label(student, text='User Management ', font='Arial 12')
    lblUserManagement.grid(row=1, column=0, padx=10)
    btnUpdateInfo = Button(student, text='Update Info ', font='Arial 12', command=updateInfo)
    btnUpdateInfo.grid(row=2, column=0, padx=10)



    lblBookManagement = Label(student, text='Book Management', font='Arial 12')
    lblBookManagement.grid(row=1, column=1, padx=10)
    btnViewBookList = Button(student, text='View book list', font='Arial 12', command=viewBookList)
    btnViewBookList.grid(row=2, column=1, padx=10)
    student.mainloop()