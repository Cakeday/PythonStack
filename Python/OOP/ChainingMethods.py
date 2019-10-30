class User:

    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def makeDeposit(self,amount):
        self.account_balance += amount
        return self

    def makeWithdrawal(self,amount):
        self.account_balance -= amount
        return self

    def displayBalance(self):
        print(self.name,self.account_balance)
        return self

    def transfer(self, transferrer, transferee, amount):
        transferrer.account_balance -= amount
        transferee.account_balance += amount
        return self


guido = User("Guido van Rossum","guidoYEET@gmaaaaail.com")
guido.makeDeposit(100).makeDeposit(100).makeDeposit(100).makeWithdrawal(90).displayBalance()

caleb = User("Caleb Reyes","sciencecamp123@gmail.com")
caleb.makeDeposit(800).makeDeposit(800).makeWithdrawal(50800).makeWithdrawal(400).displayBalance()

cameron = User("Cameron Reyes","cam@yaheezy.com")
cameron.makeDeposit(8).makeWithdrawal(7).makeWithdrawal(7).makeWithdrawal(7).displayBalance()

guido.transfer(guido, caleb, 10000).displayBalance()
caleb.displayBalance()