class BankAccount:
    #creating the constructor with helf od access modifiers
    def __init__(self,name,balance,pin):
        self.name = name #public
        self._balance = balance #protected
        self.__pin = pin #private
        
    def check_pin(self,entered_pin):
        return self.__pin == entered_pin
    
    def get_balance(self):
        return self._balance
    
    #dispalying the account information    
    def display_info(self):
        print(f"Account Holder : {self.name}")
        print(f"Available Balance: ₹{self._balance}")
        
    def withdraw(self,amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"₹{amount} withdrawn succefully..")
            else:
                print("Insufficient Balance.")
    
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully..")
        else:
            print(f"Enter any amount??")
    
    #subclass: ATM Machine interface        
class ATM(BankAccount):
    
    def __init__(self):
        self.accounts = {}
        self.logged_in_user = None
        
    def create_account(self, name,pin , balance=0):
        if name in self.accounts:
            print("Account already exists with this name.")
        else:
            self.accounts[name] = BankAccount(name,  balance, pin)
            print(f"Account for '{name}' created successfully.")

    def login(self, name, pin):
        account = self.accounts.get(name)
        if account and account.check_pin(pin):
            self.logged_in_user = account
            print(f"Welcome, {name}!")
        else:
            print("Invalid name or PIN.")

    def logout(self):
        if self.logged_in_user:
            print(f"Goodbye, {self.logged_in_user.name}!")
            self.logged_in_user = None
        else:
            print("No user is currently logged in.")

    def show_balance(self):
        if self.logged_in_user:
            self.logged_in_user.display_info()
        else:
            print("Please login first.")

    def deposit_money(self, amount):
        if self.logged_in_user:
            self.logged_in_user.deposit(amount)
        else:
            print("Please login first.")

    def withdraw_money(self, amount):
        if self.logged_in_user:
            self.logged_in_user.withdraw(amount)
        else:
            print("Please login first.")

# Simulating ATM system
atm = ATM()

# Creating multiple accounts
atm.create_account("Lynda", 1234, 5000)
atm.create_account("Alex", 4321, 10000)
print()

# Login and do transactions
atm.login("Lynda", 1234)
atm.show_balance()
atm.deposit_money(2000)
atm.withdraw_money(1500)
atm.show_balance()
atm.logout()
print()

atm.login("Alex", 4321)
atm.show_balance()
atm.withdraw_money(5000)
atm.deposit_money(1000)
atm.logout()