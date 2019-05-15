class BankAccount:
    interest_rate = 0.15
    accounts = []
#Add a class variable interest_rate  interest rate for all the accounts. 
#class variable same value for all accounts.  
#Add another class variable called accounts that starts as an empty list. This will eventually store the collection of all bank accounts in the bank.
#Add an __init__() balance to zero. Balance is stored in an instance variable.
    
    def __init__(self, initial_balance):
        self.balance = initial_balance

#Add an method deposit  number as an argument adds that amount to the account's balance.
#instance method, a single, specific account.
    def deposit(self, amount):
        self.balance += amount
        return self.balance

#Add instance method withdraw accepts number, subtracts that amount from the account's balance.
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


#+Add a class method create  a new  BankAccount().
#+adds the new object to the accounts class variable so that we can find it again in the future. 
#+This method should return the new account object. 
    @classmethod
    def create_bank_account(cls, initial_balance):
        the_bank_account = BankAccount()
        cls.accounts.append(the_bank_account)
        return the_bank_account


#Add a class method  total_funds returns the sum of all balances across all accounts in the accounts class variable.
    @classmethod
    def total_funds(cls):
        sum_of_all_funds = 0
        for account in cls.accounts:
            sum_of_all_funds += account.balance
        return sum_of_all_funds

#Add a class method called interest_time that iterates through all accounts and increases their balances according to the class interest_rate. 
#This needs to be a class method because it operates on all bank accounts
    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate


my_account = BankAccount.create_bank_account()
your_account = BankAccount.create_bank_account()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0