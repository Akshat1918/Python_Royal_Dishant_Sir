ini_bal = 0

def openAccount():
    username = input("Enter your name: ") 
    password = input("Enter the password: ")
    print("Account created successfully")
    return username, password

def deposit():
    global ini_bal
    amount = int(input("Enter the amount to deposit: "))
    if amount > 0:
        ini_bal += amount
        print("Amount deposited successfully")

def withdraw():
    global ini_bal
    amount = int(input("Enter the amount to withdraw: "))
    if amount > 0:
        if ini_bal >= amount:
            ini_bal -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

def check_balance():
    print("Your current balance is:", ini_bal)

def main():
    print("Welcome to the Bank Account Management System")
    print("1. Open Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    username = None
    password = None

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username, password = openAccount()
        elif choice == 2:
            if username:
                deposit()
            else:
                print("Please open an account first.")
        elif choice == 3:
            if username:
                withdraw()
            else:
                print("Please open an account first.")
        elif choice == 4:
            if username:
                check_balance()
            else:
                print("Please open an account first.")
        elif choice == 5:
            print("Thank you for using the Bank Account Management System")
            break
        else:
            print("Invalid choice. Please try again")

main()
