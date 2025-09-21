import random 

class Rock_Paper_Scissors():
    def __init__(self, player, computer): 
        self.player = player
        self.computer = computer
    
    def play_round(self):
        if self.player == self.computer:
            return "tie"
        
        if self.player == "rock":
            if self.computer == "scissors":
                print(f"{self.player.capitalize()} beats {self.computer.capitalize()}. PLAYER wins this round.")
                return "player"
            elif self.computer == "paper":
                print(f"{self.computer.capitalize()} beats {self.player.capitalize()}. COMPUTER wins this round.")
                return "computer"
        elif self.player == "paper":
            if self.computer == "rock":
                print(f"{self.player.capitalize()} beats {self.computer.capitalize()}. PLAYER wins this round.")
                return "player"
            elif self.computer == "scissors":
                print(f"{self.computer.capitalize()} beats {self.player.capitalize()}. COMPUTER wins this round.")
                return "computer"
        elif self.player == "scissors":
            if self.computer == "rock":
                print(f"{self.computer.capitalize()} beats {self.player.capitalize()}. COMPUTER wins this round.")
                return "computer"
            elif self.computer == "paper":
                print(f"{self.player.capitalize()} beats {self.computer.capitalize()}. PLAYER wins this round.")
                return "player"

def main():
    possible_actions = ["rock", "paper", "scissors"]

    print("WELCOME TO ROCK PAPER SISSORS!!!")
    print("First to 3 WINS!")

    computer_score = 0
    player_score = 0

    while computer_score < 3 and player_score < 3:
        user_input = input("Make your move (rock, paper, scissors) or type 'exit' to quit: ")

        if user_input == "exit":
            print("Thanks for playing!\nBYE")
            break
        elif user_input not in possible_actions:
            print("Invalid move. Try again.\n")
            continue  
        
        computer = random.choice(possible_actions)
        print(f"[Computer Chose: {computer}]")

        game = Rock_Paper_Scissors(user_input, computer)
        result = game.play_round()

        if result == "player":
            print("[Computer: 😓]")
            player_score += 1
        elif result == "computer":
            print("[Computer: 🤣🫵 ]")
            computer_score += 1
        elif result == "tie":
            print("TIE!! (Computer: 😡)")
        
        print(f"Score -> Player: {player_score} - Computer: {computer_score}")
    
    if player_score == 3:
        print("Congrats!! YOU WON THE GAME 🎉")

    if computer_score == 3:
        print("You lost! COMPUTER WON THE GAME\n [Computer: 😝]")


if __name__ == "__main__":
    main()