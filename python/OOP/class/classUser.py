class User:
    def __init__(self, name,email):
        self.name=name
        self.email=email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

tom = User("Tom","tnguyen@dupage.edu")
tuan = User("Tuan", "tuan@gmail.com")

tom.make_deposit(15).make_deposit(15).make_deposit(15)   
print("Account Mr {} has ${} in bank account".format(tom.name, tom.account_balance))

tom.make_withdrawal(2)
print(tom.account_balance)

tom.transfer(tuan, 2).transfer(tuan, 2)
print(tom.account_balance)
print(tuan.account_balance)

