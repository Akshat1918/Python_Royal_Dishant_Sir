# single level :
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class customer(person):
    def __init__(self, name, age, accno):
        super().__init__(name, age)
        self.accno = accno

# multilevel + multiple inheritance
class account(customer):
    def __init__(self, name, age, accno, balance):
        super().__init__(name, age, accno)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("New balance after withdrawal:", self.balance)

# login
class internetbanking:
    def login(self, user_id, password):
        if self.user_id == user_id and self.password == password:
            print("Login successful with user ID:", user_id)
        else:
            print("Login failed! Incorrect credentials.")
            exit()
            
# multilevel inheritance with multiple
class netbanking(account, internetbanking):
    def __init__(self, name, age, accno, balance, user_id, password, fees):
        super().__init__(name, age, accno, balance)
        self.user_id = user_id
        self.password = password
        self.fees = fees

# hierarchical
class savingsaccount(customer):
    def __init__(self, name, age, accno, balance):
        super().__init__(name, age, accno)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New balance after deposit:", self.balance)

    def withdraw(self, amount):
        charges = 0
        if self.balance > 30000:
            charges = amount * 0.20
        elif self.balance > 20000:
            charges = amount * 0.10
        else:
            charges = 0

        total = amount + charges
        if total > self.balance:
            print("Insufficient balance including charges!")
        else:
            self.balance -= total
            print(f"Withdrawal: {amount}, Charges: {charges}, New Balance: {self.balance}")

class currentaccount(customer):
    def current_feature(self):
        print("Current account feature")

print("============== Task 1: Net Banking User ==============")
user = netbanking("Akshat", 19, 1234567890, 25000, "user123", "pass123", 100)
user.login("user1234", "pass123") 
user.deposit(3000)
user.withdraw(1500)

print("\n============== Task 2: Savings Account (Above 30,000) ==============")
s1 = savingsaccount("Suresh", 20, 9999999999, 35000)
s1.deposit(2000)
s1.withdraw(5000)  

print("\n============== Task 2: Savings Account (Above 20,000) ==============")
s2 = savingsaccount("Mukesh", 21, 8888888888, 25000)
s2.deposit(1000)
s2.withdraw(4000)  

print("\n============== Task 2: Savings Account (Below 20,000) ==============")
s3 = savingsaccount("Ramesh", 22, 7777777777, 15000)
s3.deposit(500)
s3.withdraw(2000)  