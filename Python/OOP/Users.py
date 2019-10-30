class User:

    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def makeDeposit(self,amount):
        self.account_balance += amount

    def makeWithdrawal(self,amount):
        self.account_balance -= amount

    def displayBalance(self):
        print(self.name,self.account_balance)

    def transfer(self, transferrer, transferee, amount):
        transferrer.account_balance -= amount
        transferee.account_balance += amount


guido = User("Guido van Rossum","guidoYEET@gmaaaaail.com")
guido.makeDeposit(100)
guido.makeDeposit(100)
guido.makeDeposit(100)
guido.makeWithdrawal(90)
guido.displayBalance()

caleb = User("Caleb Reyes","sciencecamp123@gmail.com")
caleb.makeDeposit(800)
caleb.makeDeposit(800)
caleb.makeWithdrawal(50800)
caleb.makeWithdrawal(400)
caleb.displayBalance()

cameron = User("cameron Reyes","cam@yaheezy.com")
cameron.makeDeposit(8)
cameron.makeWithdrawal(7)
cameron.makeWithdrawal(7)
cameron.makeWithdrawal(7)
cameron.displayBalance()

guido.transfer(guido, caleb, 10000)
guido.displayBalance()
caleb.displayBalance()