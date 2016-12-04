
from datetime import datetime

class Account(object):

    def __init__(self):
        self.__balance = 0
        self.__history = []

    def deposit(self, amount):
        self.__balance += amount
        history_entry = ('CREDIT', amount, str(datetime.now()))
        self.__history.append(history_entry)


    def withdraw(self, amount):
        self.__balance -= amount
        history_entry = ('DEBIT', amount, str(datetime.now()))
        self.__history.append(history_entry)

    def balance(self):
        return self.__balance

    def history(self):
        return list(self.__history)

if __name__ == "__main__":

    acc_a = Account()
    acc_a.deposit(250)
    acc_a.deposit(10)
    acc_a.withdraw(100)
    print acc_a.balance() # 160
    print acc_a.history() # [('CREDIT', 250, '2016-12-04 14:28:55.949813'),
                          # ('CREDIT', 10, '2016-12-04 14:28:55.950225'),
                          # ('DEBIT', 100, '2016-12-04 14:28:55.950248')]
    acc_b = Account()
    acc_b.withdraw(200)
    print acc_b.balance() # -200
    print acc_b.history() # [('DEBIT', 200, '2016-12-04 14:30:02.766961')]

