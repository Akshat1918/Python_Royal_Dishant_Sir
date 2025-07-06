import random as r

l1 = ["stone", "paper", "scissors"]

userScore = 0
computerScore = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Press:\n1 for Stone\n2 for Paper\n3 for Scissors\n4 to quit.\n")

while True:
    userInput = input("Enter your choice (1/2/3) or (4) to quit: ").lower()

    if userInput == "4":
        break

    match userInput:
        case "1":
            userChoice = "stone"
        case "2":
            userChoice = "paper"
        case "3":
            userChoice = "scissors"
        case _:
            print("Invalid input. Please try again.")
            continue

    computerChoice = r.choice(l1)
    print(f"You chose: {userChoice}")
    print(f"Computer chose: {computerChoice}")

    if userChoice == computerChoice:
        print("It's a tie!\n")
    elif (userChoice == "stone" and computerChoice == "scissors") or \
         (userChoice == "paper" and computerChoice == "stone") or \
         (userChoice == "scissors" and computerChoice == "paper"):
        print("You win!\n")
        userScore += 1
    else:
        print("Computer wins!\n")
        computerScore += 1

print("\nFinal Scores:")
print("User score:", userScore)
print("Computer score:", computerScore)
