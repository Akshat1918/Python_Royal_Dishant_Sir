import random as r

l1 = [1, 2, 3, 4, 5, 6]

userScore = 0
computerScore = 0
totalRounds = 10

print("Welcome to the Dice Throw Game!")
print("Press:\n1 to throw the dice\n2 to quit.\n")

while totalRounds > 0:
    try:
        userChoice = int(input("Enter your choice (1 to throw, 2 to quit): "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        continue

    if userChoice == 2:
        break

    if userChoice == 1:
        userInput = int(input("Enter a number between 1 and 6: "))
        computerInput = r.choice(l1)

        print("You rolled:", userInput)
        print("Computer rolled:", computerInput)

        if userInput > computerInput:
            print("You win this round!")
            userScore += 1
        elif userInput < computerInput:
            print("Computer wins this round!")
            computerScore += 1
        else:
            print("It's a tie!")

        totalRounds -= 1
    else:
        print("Invalid input. Please enter 1 or 2.")

print("\nFinal Scores:")
print("Your score:", userScore)
print("Computer's score:", computerScore)