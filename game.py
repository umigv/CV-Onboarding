import random

class NumberGuessingGame:
    def __init__(self, lower=1, upper=100, max_attempts=10):
        self.lower = lower
        self.upper = upper
        self.max_attempts = max_attempts
        self.secret_number = random.randint(lower, upper)
        self.attempts = 0
        self.is_over = False

    def make_guess(self, guess):
        self.attempts +=1
        if guess == self.secret_number:
            self.is_over = True
            return f"Correct! The number was {self.secret_number}. You won in {self.attempts} tries."
        elif guess < self.secret_number:
            return "Too low!"
        else:
            return "Too high!"

    def has_attempts_left(self):
        return self.attempts < self.max_attempts


def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    game = NumberGuessingGame()

    while not game.is_over and game.has_attempts_left():
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        feedback = game.make_guess(guess)
        print(feedback)

    if not game.is_over:
        print(f"Game over! The number was {game.secret_number}.")


if __name__ == "__main__":
    play()