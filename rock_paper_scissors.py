import random

class gameFunctions:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, player, computer):
        if player == "rock" and computer == "scissors":
            return "player"
        elif player == "paper" and computer == "rock":
            return "player"
        elif player == "scissors" and computer == "paper":
            return "player"
            
        return "computer"


class gameRunner:
    def __init__(self):
        self.functions = gameFunctions()
        self.playerPoints = 0 
        self.computerPoints = 0

    def start(self):
        print("welcome to rock, paper, scissors!")
        self.game_loop()

    def game_loop(self):
        while True:
            player_move = input("\nenter rock, paper, scissors (or 'quit'): ").lower()
            if player_move == "quit":
                break
                
            if player_move not in self.functions.choices:
                print("invalid. try again.")
                continue

            comp_move = self.functions.get_computer_choice()
            print(f"computer chose: {comp_move}")

            result = self.functions.determine_winner(player_move, comp_move)
            self.update_score(result)
            
        self.end_game()

    def update_score(self, winner):
        if winner == "player": 
            self.playerPoints+=1
            print("you win this round")
        elif winner == "computer":
            self.computerPoints+=1
            print("you lost this round")
        else:
            print("it's a tie")

    def end_game(self):
        if self.playerPoints == 0:
            print("see you next time")

        else:
            print("\n--- final score ---")
            print(f"player: {self.playerPoints} | computer: {self.computerPoints}")
            if self.playerPoints > self.computerPoints:
                print("you won!")
            else:
                print("you lost :(")
    
    

game = gameRunner()
game.start()
