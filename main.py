from db import *


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
        print(f'account name: {row[1]}')
        print(f'balance: {row[2]}')
    def addAccount(self):
        conn.execute('INSERT INTO account values (?, ?, ?)', (1, self.account_name, self.balance,))
        conn.commit()
    def deposit(self):
        money = input('Nhập số bạn muốn nạp:')
        self.balance = self.balance + int(money)
        print(f'Balance: {self.balance}')
        data = {'no':'', 'type': '', 'money':''}
        if len(self.storage) == 0:
            data['no'] = 1
        else:
            data['no'] = self.storage[-1]['no'] + 1
        data['type'] = 'deposit'
        data['money'] = money
        self.storage.append(data)
    def withdraw(self):
        money = input('Nhập số tiền bạn muốn rút:')
        if self.balance > int(money):
            self.balance = self.balance - int(money)
            print(f'balance:{self.balance}')
            data = {'no': '', 'type': '', 'money': ''}
            if len(self.storage) == 0:
                data['no'] = 1
            else:
                data['no'] = self.storage[-1]['no'] + 1
            data['type'] = 'withdraw'
            data['money'] = money
            self.storage.append(data)
        else:
            print("Your balance doesn't have enough money to withdraw")



    def history(self):
        print(f'Your history transaction:')
        for i in self.storage:
            print(f"No.{i['no']} - {i['type']} - {i['money']}")
        print(f'Balance: {self.balance}')
createTable()
account1 = Ewallet('Than Duc Kien', 0)
account1.addAccount()
# account1.view()
# account1.deposit(2000)
# account1.withdraw(1000)
# account1.history()
luachon = 0

while luachon >= 0:
    if luachon ==1:
        account1.view()
    elif luachon ==2:
        account1.deposit()
    elif luachon ==3:
        account1.withdraw()
    elif luachon ==4:
        account1.history()
    print('Chọn chức năng: ')
    print('1: Xem số dư')
    print('2: Nạp tiền')
    print('3: Rút tiền')
    print('4: Lịch sử giao dịch')
    print('0: Thoát')
    luachon = int(input('Nhập số theo Menu trên: '))
    if luachon == 0:
        break