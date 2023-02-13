from db import *
from tkinter import *
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



        # self.storage.append(data)
    def withdraw(self):
        money = input('Nhập số tiền bạn muốn rút:')
        if self.balance > int(money):
            self.balance = self.balance - int(money)
            print(f'balance:{self.balance}')
            htype = 'withdraw'
            Id = 1
            conn.execute('UPDATE account set balance = ? WHERE id= ?',(self.balance, Id))
            conn.execute('INSERT INTO history (htype, money) VALUES(?,?)',(htype, money))
            # data = {'no': '', 'type': '', 'money': ''}
            # if len(self.storage) == 0:
            #     data['no'] = 1
            # else:
            #     data['no'] = self.storage[-1]['no'] + 1
            # data['type'] = 'withdraw'
            # data['money'] = money
            # self.storage.append(data)

        else:
            print("Your balance doesn't have enough money to withdraw")



    def history(self):
        print(f'Your history transaction:')
        cur = conn.execute('SELECT * FROM history')
        row = cur.fetchall()
        for i in row:
            print(i)

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