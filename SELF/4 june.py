class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
        else:
            self.balance += amount
            print("Deposited amount:", amount)
            print("New balance:", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif self.balance - amount < 10000:
            print("Insufficient balance. Minimum balance of 10000 must be maintained.")
        else:
            self.balance -= amount
            print("Withdrawn amount:", amount)
            print("New balance:", self.balance)
    
    def check_balance(self):
        print("Balance:", self.balance) 

    def logout(self):
        print("Thank you for using the bank services. Goodbye!")



b = Bank("Hemali", 7201000127890, 25000)

print("Welcome to the Bank!")
print("Choose an option:")
print("d: Deposit")
print("w: Withdraw")
print("b: Check Balance")
print("q: Quit")


switch = input("Enter your choice: ").strip().lower()


if switch == 'd': 
    b.deposit()
elif switch == 'w':
    b.withdraw()
elif switch == 'b':
    b.check_balance()
elif switch == 'q':
    b.logout()
else:
    print("Invalid option selected. Please choose 'd', 'w', 'b', or 'q'.")