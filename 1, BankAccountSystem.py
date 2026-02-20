class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)  
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance") 
    def display_balance(self):
        print("Name:", self.name)
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)
acc = BankAccount("Abhiraj", 101, 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.display_balance()