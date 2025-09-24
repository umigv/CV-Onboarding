import random

def result(choice):
    computerResult = random.randint(1,3)
    if computerResult==1:
        computerChoice = "Rock"
    elif computerResult==2:
        computerChoice = "Paper"
    else:
        computerChoice = "Scissors"
    print("Computer Choice: " + computerChoice)
    computerChoice = computerChoice.lower()
    choice = choice.strip().lower()
    if choice == "rock" and computerChoice == "paper":
        return "Computer Won"
    elif choice == "paper" and computerChoice == "scissors":
        return "Computer Won"
    elif choice == "scissors" and computerChoice == "rock":
        return "Computer Won"
    elif choice == computerChoice:
        return "draw"
    else:
        return "Player Won"

print("Rock, Paper, Scissors")
print("First to 3")
playerWinCount = 0
computerWinCount  = 0

while playerWinCount != 3 and computerWinCount != 3:
    choice = input("Enter your choice: ")
    finalResult = result(choice)
    if finalResult=="Computer Won" :
        computerWinCount+=1
    elif finalResult=="Player Won":
        playerWinCount+=1
    print(finalResult)
    print("Player Score: ", playerWinCount)
    print("Computer Score: ", computerWinCount)
if playerWinCount == 3:
    print("Player won the game")
elif computerWinCount==3:
    print("Computer won the game")



