from tkinter import *

root = Tk()
root.title('E-wallet')
root.geometry('500x500')

lblTitle = Label(root, text='E-wallet')
lblTitle.grid(column=0, row=0, columnspan=3)

lblMenu1 = Label(root, text='Chon chuc nang')
lblMenu1.grid(column=0, row=1)

root.mainloop()