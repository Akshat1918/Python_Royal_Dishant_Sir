class bank:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        if amount >= 0:
            self.balance = amount
        else:
            print("Invalid balance. Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Invalid withdrawal. Check your balance or amount.")
    


b=bank(5000)
print("Initial Balance:", b.get_balance())
b.deposit(2000)
print("After Deposit:", b.get_balance())
b.withdraw(3000)
print("After Withdrawal:", b.get_balance())
b.set_balance(10000)
print("Updated Balance:", b.get_balance())
b.withdraw(1500) 
print("After Withdrawal Attempt:", b.get_balance())
b.set_balance(-500)  
print("Final Balance:", b.get_balance())

