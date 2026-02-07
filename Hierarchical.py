class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Deposited:", self.amount)
    
    def withdraw(self,amount):
        if amount < self.balance:
            self.amount -= amount
            print("withdrawn:", self.amount)
        else:
            print("insufficient balance")

    def display_balance(self):
        print("Balance:", self.amount)

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate,):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("interested add:", interest)
        print("New balance:", self.balance)


class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit, account_holder, balance):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self,amount):

