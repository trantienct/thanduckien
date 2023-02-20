from db import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
def printHello():
    print('Hello')

class Ewallet:
    storage = []
    def __init__(self, account_name, balance ):
        self.account_name = account_name
        self.balance = balance
    def view(self):
        cur = conn.execute('SELECT * FROM account')
        row = cur.fetchone()
        view = Toplevel(root)
        view.geometry('250x100')
        lblAcountName = Label(view, text="Account Name: " + self.account_name)
        lblAcountName.grid(column=0, row=0, sticky='w')
        lblBalance = Label(view, text="Balance: " + str(self.balance) )
        lblBalance.grid(column=0, row=1, sticky='w')
        view.mainloop()
    def addAccount(self):
        conn.execute('INSERT INTO account (account_name, balance) values (?,?) ', (self.account_name, self.balance,))
        conn.commit()
    def deposit(self):
        def depositMoney():
            htype = "deposit"
            money = entry.get()
            self.balance = self.balance + int(money)
            Id = 1
            conn.execute('UPDATE account SET balance = ? WHERE id =?', (self.balance, Id))
            conn.execute('INSERT INTO history (htype, money) VALUES(?,?)', (htype, money,))
            conn.commit()
            deposit.withdraw()
        money = ''
        deposit = Toplevel(root)
        deposit.geometry('200x200')
        lblText = Label(deposit, text='Your deposit money: ')
        lblText.grid(row=0, column=0)
        entry = Entry(deposit, textvariable=money)
        entry.grid(row=0, column=1)
        btnSubmit = Button(deposit, text='Submit', command=depositMoney)
        btnSubmit.grid(row=1, column=0)

    def withdraw(self):
        def withdrawMoney():
            htype = 'withdraw'
            money = entry.get()
            if self.balance > int(money):
                self.balance = self.balance - int(money)
                Id = 1
                conn.execute('UPDATE account set balance = ? WHERE id= ?', (self.balance, Id))
                conn.execute('INSERT INTO history (htype, money) VALUES(?,?)', (htype, money))
                conn.commit()
                withdraw.withdraw()
                # data = {'no': '', 'type': '', 'money': ''}
                # if len(self.storage) == 0:
                #     data['no'] = 1
                # else:
                #     data['no'] = self.storage[-1]['no'] + 1
                # data['type'] = 'withdraw'
                # data['money'] = money
                # self.storage.append(data)

            else:
                messagebox.showinfo('Error', 'You dont have enough money ')

        money = ''
        withdraw = Toplevel(root)
        withdraw.geometry('200x200')
        lblText = Label(withdraw, text = 'Your withdraw money: ')
        lblText.grid(row = 0, column=0)
        entry = Entry(withdraw, textvariable=money)
        entry.grid(row=0, column=0)
        btnSubmit = Button(withdraw, text='Submit', command=withdrawMoney)
        btnSubmit.grid(row=1, column=0)



    def history(self):
        print(f'Your history transaction:')
        cur = conn.execute('SELECT * FROM history')
        row = cur.fetchall()
        for i in row:
            print(i)
        his = Toplevel(root)
        his.title('HISTORY')
        his.geometry('500x500')
        history = ttk.Treeview(his, show='headings')
        #Heading
        #show=
        #...
        history.grid(column=0, row=0)
        history['columns'] = ('id', 'type', 'money')
        history.column('id', width=100)
        history.column('type', width=200)
        history.column('money', width=200)

        history.heading('id', text = 'ID')
        history.heading('type', text='type')
        history.heading('money', text='money')
        cur = conn.execute('SELECT * FROM history')
        row = cur.fetchall()
        for i in row:
            history.insert(parent='', index=0, values= (i[0], i[1], i[2]))
        his.mainloop()




# createTable()

# account1.addAccount()
# # account1.view()
# # account1.deposit(2000)
# # account1.withdraw(1000)
# # account1.history()
# luachon = 0
#
# while luachon >= 0:
#     if luachon ==1:
#         account1.view()
#     elif luachon ==2:
#         account1.deposit()
#     elif luachon ==3:
#         account1.withdraw()
#     elif luachon ==4:
#         account1.history()
#     print('Chọn chức năng: ')
#     print('1: Xem số dư')
#     print('2: Nạp tiền')
#     print('3: Rút tiền')
#     print('4: Lịch sử giao dịch')
#     print('0: Thoát')
#     luachon = int(input('Nhập số theo Menu trên: '))
#     if luachon == 0:
#         break