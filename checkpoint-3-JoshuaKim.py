import random

class NumberGuessingGame:
    def __init__(self, low=1, high=100):
        
        self.low = low
        self.high = high
        self.reset_game()

    def reset_game(self):
       
        self.target = random.randint(self.low, self.high)
        self.guesses = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        playing = True

        while playing:
            print(f"\nGuess a number between {self.low} and {self.high}.")
            while True:
                try:
                    guess = int(input("Enter guess: "))
                except ValueError:
                    print("Your number is not valid, try again.")
                    continue

                self.guesses += 1

                if guess < self.target:
                    print("Too low, try again!")
                elif guess > self.target:
                    print("Too high, try again!")
                else:
                    print(f"Correct! You guessed it in {self.guesses} tries.")
                    break

            
            again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if again == "y":
                self.reset_game()
            else:
                print("Thanks for playing! Have good day!")
                playing = False


if __name__ == "__main__":
   
    game = NumberGuessingGame(1, 25)
    game.play()