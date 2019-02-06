class Bank_Account:
    def __init__(self, rate,balance):
        self.rate = rate
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.rate)
        return self

# bank1 = Bank_Account(0.01,0)
# bank2 = Bank_Account(0.02,0)

# bank1.deposit(100).deposit(200).deposit(100).withdraw(150).yield_interest()
# bank1.display_account_info()

# bank2.deposit(50).deposit(12).deposit(15).withdraw(5).yield_interest()
# bank2.display_account_info()

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account = Bank_Account(0.05,0)
    
    # Deposit to one account default
    def update_deposit(self,dollar):
        self.account.deposit(dollar)
        self.account.yield_interest()
        self.account.display_account_info()
        return self

    # withdraw to one account default
    def update_withdraw(self,dollar):
        self.account.withdraw(dollar)
        self.account.yield_interest()
        self.account.display_account_info()
        return self
        

user1 = User("Tom", "tom@gmail.com")
user1.update_deposit(10)
user1.update_withdraw(12)

print(f"Mr {user1.name}")