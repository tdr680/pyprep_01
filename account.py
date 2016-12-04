
from datetime import datetime

class Account(object):

    __number = 1000

    def __init__(self):
        self.__balance = 0
        self.__history = []
        self.__number = self.nextNumber()

    def deposit(self, amount):
        self.__balance += amount
        history_entry = ('CREDIT', amount, str(datetime.now()))
        self.__history.append(history_entry)

    def withdraw(self, amount):
        self.__balance -= amount
        history_entry = ('DEBIT', amount, str(datetime.now()))
        self.__history.append(history_entry)

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return list(self.__history)

    @property
    def number(self):
        return self.__number

    @classmethod
    def nextNumber(cls):
        cls.__number += 1
        return cls.__number

    def __str__(self):
        str = "Account: {0}\n".format(self.__number)
        str += "Balance: {0}\n".format(self.__balance)
        if len(self.__history) > 0:
            str += "History:\n"
            for e in self.__history:
                str += "{0}\t{1}\t{2}\n".format(e[0], e[1], e[2])
        return str


class YouthAccount(Account):

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('negative balance not allowed for youth accounts')
        Account.withdraw(self, amount)


if __name__ == "__main__":

    acc_a = Account()
    acc_a.deposit(250)
    acc_a.deposit(10)
    acc_a.withdraw(100)
    print acc_a
    """
Account: 1001
Balance: 160
History:
CREDIT	250	2016-12-04 15:21:20.035965
CREDIT	10	2016-12-04 15:21:20.036392
DEBIT	100	2016-12-04 15:21:20.036406
    """

    acc_b = YouthAccount()
    acc_b.withdraw(200) # Throws ValueError: negative balance not allowed for youth accounts
    print acc_b
    """
Account: 1002
Balance: -200
History:
DEBIT	200	2016-12-04 15:21:20.036485
    """

    acc_c = Account()
    print acc_c
    """
Account: 1003
Balance: 0
    """