import random

class RPS:
    choices = ['rock', 'paper', 'scissors']
    
    def play(self):
        print("Rock, Paper, Scissors")
        wins = 0
        while True:
            player = input("\nYou: ").strip().lower()
            if player == 'quit':
                break
            if player not in self.choices:
                print("Invalid! Choose rock, paper or scissors")
                continue

            computer = random.choice(self.choices)
            print(f"Computer: {computer}")
            
            if player == computer:
                print("Tie!")
            elif (player, computer) in [('rock','scissors'), ('paper','rock'), ('scissors','paper')]:
                print("You win!")
                wins += 1
            else:
                print("Computer wins!")
                
        print(f"\nYou won {wins} times. Bye!")

if __name__ == "__main__":
    game = RPS()
    game.play()