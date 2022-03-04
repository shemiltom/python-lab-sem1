""""2. Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank."""
class Bank_Account:
    name=""
    act=0
    act_type=""
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Banking")
        self.name=input("Enter your name             : ")
        self.act=int(input("Enter the account number : "))
        self.act_type=input("Enter the account type       : ")
        print("\nWelcome ",self.name)
        print(self.act_type,"Account")
    def deposit(self):
        amt = float(input("Enter amount to be Deposited: "))
        self.balance += amt
        print("Amount Deposited:", amt)

    def withdraw(self):
        amt = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amt:
            self.balance -= amt
            print("You Withdrew:", amt)
        else:
            print("Insufficient balance  ")

    def display(self):
        print("Net Available Balance=", self.balance)
        print("Thanks ",self.name)
b = Bank_Account()
b.deposit()
b.withdraw()
b.display()