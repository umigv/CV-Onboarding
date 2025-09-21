# Lincoln Jones Simple game in Python for programming checkpoint

import os, msvcrt, sys

class Game:
    def __init__(self):
        self.state = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.cursor = [0, 0]
        self.player = "X"
        self.updated = True

    def evaluate_winners(self):
        # check rows
        for row in self.state:
            if row[0] != " " and row[0] == row[1] == row[2]:
                return row[0]

        # check columns
        for c in range(3):
            if self.state[0][c] != " " and self.state[0][c] == self.state[1][c] == self.state[2][c]:
                return self.state[0][c]

        # check diagonals
        if self.state[0][0] != " " and self.state[0][0] == self.state[1][1] == self.state[2][2]:
            return self.state[0][0]
        if self.state[0][2] != " " and self.state[0][2] == self.state[1][1] == self.state[2][0]:
            return self.state[0][2]

        return None
                        


    def place(self):
        r, c = self.cursor
        if self.state[r][c] == " ":
            self.state[r][c] = self.player
            # toggle player for next placement
            self.player = "O" if self.player == "X" else "X"
            self.updated = True

    def pretty_print_state(self):
        os.system("cls")  # clear screen on Windows
        print("Use arrow keys to move | Press 'K' to place | Press 'O' to quit")
        print(f"Current player: {self.player}")
        print("-----------")
        for i, row in enumerate(self.state):
            line = []
            for j, cell in enumerate(row):
                disp = cell
                if i == self.cursor[0] and j == self.cursor[1]:
                    disp = f"[{cell if cell != ' ' else ' '}]"
                else:
                    disp = f" {cell} "
                line.append(disp)
            print("|".join(line))
            print("-----------")


def main():
    game = Game()
    running = True
    while running:
        if game.updated:
            game.pretty_print_state()
            game.updated = False

        key = msvcrt.getch()

        if key == b"\xe0":
            second = msvcrt.getch()
            if second == b"H":  # Up
                if game.cursor[0] > 0:
                    game.cursor[0] -= 1
                    game.updated = True
            elif second == b"P":  # Down
                if game.cursor[0] < 2:
                    game.cursor[0] += 1
                    game.updated = True
            elif second == b"K":
                if game.cursor[1] > 0:
                    game.cursor[1] -= 1
                    game.updated = True
            elif second == b"M":  # Right
                if game.cursor[1] < 2:
                    game.cursor[1] += 1
                    game.updated = True

        else:
            try:
                ch = key.decode().lower()
            except Exception:
                ch = ""

            if ch == "o":
                sys.exit()
            elif ch == "k":
                game.place()

        winner = game.evaluate_winners()
        if winner:
            game.pretty_print_state()
            print(f"{winner} has won!")
            running = False

if __name__ == "__main__":
    main()