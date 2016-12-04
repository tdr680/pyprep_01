
class Account(object):

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


if __name__ == "__main__":

    acc_a = Account()
    acc_a.deposit(250)
    acc_a.deposit(10)
    acc_a.withdraw(100)
    print acc_a.balance # 160

    acc_b = Account()
    acc_b.withdraw(200)
    print acc_b.balance # -200

