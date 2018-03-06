import random

class BankAccount:
    #constructor
    def __init__(self, name, bal):
        self.name=name
        self.balance=bal

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def __str__(self, name):
        return " Owner: " + self.name + "\tBalance: $" + str(self.balance)

marysAcct=BankAccount("Mary Jones" , 300)
lisasAcct=BankAccount("Lisa Barnes", 425.25)
print(marysAcct.balance)
print(lisasAcct.balance)

accounts=[]
for i in range(0, 100):
    acct=BankAccount("Name", random.randrange(1, 10000))
    accounts.append(acct)

for a in accounts:
    print(a)