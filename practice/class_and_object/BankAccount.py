# Create a BankAccount class with name and balance.

# Add a method deposit(amount) and withdraw(amount) with validation.

# Take user input for 3 accounts, allow deposit/withdraw, and print final balances.

class BankAccount:
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0:
           self.balance += amount
           print(f"{self.name} has deposited ₹{amount}.. \nyour current balance ₹{self.balance}\n--------------")
        else:
            print("Please deposit some amount(you entered amount as zero)\n----------------")
            
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nyour balance ₹{self.balance} after withdrawing ₹{amount}\n------------------")
        else:
            print(f"your balance ₹{self.balance}.. insufficient balance --- entered amount ₹{amount}\n----------------")
    
    def __str__(self):
        return f"Name of Accound Holder: {self.name} \nBalance: ₹{self.balance} \n-----------------  "

bank1 = BankAccount("Lynda",2000)
bank1.deposit(1000)
bank1.withdraw(1500)

bank2 = BankAccount("princy",1000)
bank2.deposit(500)
bank2.withdraw(2000)

account = [bank1,bank2]

print("\nFinal deposits:\n")
for acc in account:
    print(acc)