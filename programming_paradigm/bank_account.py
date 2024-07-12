#create a BankAccount class
class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance  
    #define deposit given amount
    def deposit(self, amount):
        self.amount = amount
        self.account_balance + amount

    #define withdraw given amount
    def withdraw(self, amount):
        self.amount = amount
        if self.account_balance >= amount:
            self.account_balance - amount
            return True
        else:
            return False

    #define display_balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
