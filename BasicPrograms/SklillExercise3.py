class bankaccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit of rs {amount} successful")
        else:
            print("invalid deposit amount")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"withdraw of RS.{amount}successful.")
        else:
            print("invalid withdraw  amount")
    def bankfees(self):
        fees=0.05*self.balance
        self.balance-=fees
        print(f"bank of RS{fees}appplied")
    def display(self):
        print(f"AccountNumber.{self.accountNumber}")
        print(f"AccountHolder.{self.name}")
        print(f"balance is {self.balance}")
account1=bankaccount(accountNumber=123456,name="john Doe",balance=1000)
account1.display()
account1.deposit(500)
account1.bankfees()
account1.display()

