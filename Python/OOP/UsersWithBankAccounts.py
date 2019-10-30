class User:

    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(interest=0.02, balance=0)

    def makeDeposit(self,amount):
        self.account.balance += amount
        return self

    def makeWithdrawal(self,amount):
        self.account.balance -= amount
        return self

    def displayBalance(self):
        print(self.name,self.account.balance)
        return self

    def transfer(self, transferrer, transferee, amount):
        transferrer.account.balance -= amount
        transferee.account.balance += amount
        return self

    def newAccount(self):
        self.savings = BankAccount(interest=0.10, balance=1000)
        print(self.savings.balance)


class BankAccount:
    def __init__(self, interest, balance):
        self.balance = balance
        self.interest = interest

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



guido = User("Guido van Rossum","guidoYEET@gmaaaaail.com")
guido.makeDeposit(100).makeDeposit(100).makeDeposit(100).makeWithdrawal(90).displayBalance()
guido.newAccount()

# caleb = User("Caleb Reyes","sciencecamp123@gmail.com")
# caleb.makeDeposit(800).makeDeposit(800).makeWithdrawal(50800).makeWithdrawal(400).displayBalance()

# cameron = User("Cameron Reyes","cam@yaheezy.com")
# cameron.makeDeposit(8).makeWithdrawal(7).makeWithdrawal(7).makeWithdrawal(7).displayBalance()

# guido.transfer(guido, caleb, 10000).displayBalance()
# caleb.displayBalance()


# account1 = BankAccount(100)
# account1.deposit(50).deposit(80).deposit(20).withdraw(100).yieldInterest().display()

# account2 = BankAccount(500)
# account2.deposit(30).deposit(40).withdraw(10).withdraw(5).withdraw(10).withdraw(15).yieldInterest().display()





