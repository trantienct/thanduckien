from tkinter import *
from main import *

root.title('E-wallet')
root.geometry('500x500')
account1 = Ewallet('Than Duc Kien', 0)

lblTitle = Label(root, text='E-wallet')
lblTitle.grid(column=0, row=0, columnspan=3)

btnView = Button(root, text='View', command=account1.view)
btnView.grid(column=0, row=1)

btnDeposit = Button(root, text='Deposit', command=account1.deposit)
btnDeposit.grid(column=1, row=1)

btnWithdraw = Button(root, text='Withdraw', command=account1.withdraw)
btnWithdraw.grid(column=2, row=1)

btnHis = Button(root, text='History', command=account1.history())
btnHis.grid(column=3, row=1)


root.mainloop()