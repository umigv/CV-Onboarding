import random
class rpsGame:
    def __init__(user):
        user.wins = 0
        user.losses = 0
        user.ties = 0
        user.moves = ["r", "p", "s"]
        user.names = {"r": "rock", "p": "paper", "s": "scissors"}
        user.beats = {"r": "s", "s": "p", "p": "r"}

    def get_user_move(user):
        userChoice = input("Enter your move (r/p/s or q to quit)").strip().lower()
        if userChoice == "q":
            return "q"
        if userChoice in ["r", "p", "s"]:
            return userChoice
        print("Invalid input\n")
        return None

    def play_round(user, move):
        computer = random.choice(user.moves)
        print(f"User: {user.names[move]}  Computer: {user.names[computer]}")

        if move == computer:
            user.ties += 1
            print("Tie!\n")
        elif user.beats[move] == computer:
            user.wins += 1
            print("You win!\n")
        else:
            user.losses += 1
            print("You lose!\n")

    def run(user):
        print("rps begins\n")
        while True:
            move = user.get_user_move()
            if move == "q":
                break
            if move is None:
                continue
            user.play_round(move)

        total = user.wins + user.losses + user.ties
        print(f"Total Round: {total}  Win: {user.wins}  Lose: {user.losses}  Tie: {user.ties}")


if __name__ == "__main__":
    rpsGame().run()