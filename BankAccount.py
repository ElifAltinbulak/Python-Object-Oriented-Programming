"""Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class."""
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def Deposit(self,deposit):
        return self.balance-deposit
    def Withdrawal(self,withdrawal):
        return self.balance+withdrawal
    def bankFees(self):
        return (self.balance*5)/100
    def display(self):
        print(f"Deposit:{self.Deposit(10)}\nWithdrawal:{self.Withdrawal(10)}\nBankFees:{self.bankFees()}")
b1=BankAccount(100,"name",1999)
b1.display()
