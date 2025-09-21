import random

class Player:
    def game():
        random_int = int(random.randint(1, 10))
        user_input = input("Guess a random number from 1-10 inclusive: ")
        user_int = int(user_input)

        while (random_int != user_int):
            if (random_int > user_int):
                user_int = int(input("Guess higher: "))
            else:
                user_int = int(input("Guess lower: "))

        print("You guessed right!")

def main():
    player_1 = Player()
    player_1.game()

