class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.interest = .11

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if amount<0:
            print("Insufficient funds: Charging a $5 fee")
            amount -=5
        return self

    def display(self):
        print(self.balance)
        return self

    def yieldInterest(self):
        print("Heres the value before interest: ",self.balance)
        self.balance += self.interest*self.balance
        return self



account1 = BankAccount(100)
account1.deposit(50).deposit(80).deposit(20).withdraw(100).yieldInterest().display()

account2 = BankAccount(500)
account2.deposit(30).deposit(40).withdraw(10).withdraw(5).withdraw(10).withdraw(15).yieldInterest().display()

