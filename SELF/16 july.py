from abc import ABC, abstractmethod

class ATM(ABC):
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    @abstractmethod
    def deposit(self, amt):
        pass

    @abstractmethod
    def authenticate(self, pin, accno):
        pass

    @abstractmethod
    def withdraw(self, amt):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(ATM):
    def __init__(self, name, age, balance=0):
        super().__init__(name, age, balance)
        self.pin = 1234
        self.accno = 79120001432
        self.authenticated = False

    def authenticate(self, pin, accno):
        if pin == self.pin and accno == self.accno:
            self.authenticated = True
            print(f"\nAuthentication Successful. Welcome {self.name}!")
        else:
            self.authenticated = False
            print("\nInvalid PIN or Account Number.")

    def deposit(self, amt):
        if self.authenticated:
            self.balance += amt
            print(f"₹{amt} Deposited Successfully.")
        else:
            print("Please authenticate first.")

    def withdraw(self, amt):
        if self.authenticated:
            if amt <= self.balance:
                self.balance -= amt
                print(f"₹{amt} Withdrawn Successfully.")
            else:
                print("Insufficient Balance.")
        else:
            print("Please authenticate first.")

    def check_balance(self):
        if self.authenticated:
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Please authenticate first.")


# ===== MENU-DRIVEN PROGRAM =====
name = input("Enter your name: ")
age = int(input("Enter your age: "))
user = SBI(name, age, balance=50000)

while True:
    print("\n====== SBI ATM MENU ======")
    print("1. Authenticate")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        try:
            pin = int(input("Enter your PIN: "))
            accno = int(input("Enter your Account Number: "))
            user.authenticate(pin, accno)
        except:
            print("Invalid Input Format. Please enter numbers only.")
    elif choice == '2':
        try:
            amt = float(input("Enter amount to deposit: "))
            user.deposit(amt)
        except:
            print("Enter a valid number.")
    elif choice == '3':
        try:
            amt = float(input("Enter amount to withdraw: "))
            user.withdraw(amt)
        except:
            print("Enter a valid number.")
    elif choice == '4':
        user.check_balance()
    elif choice == '5':
        print("Thank you for using SBI ATM.")
        break
    else:
        print("Invalid Option. Try again.")
