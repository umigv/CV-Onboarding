import os

class TicTacToe:
    def __init__(self, board):
        self.board = board

    def draw(self):
        for i in range(0, 3):
            for letter in self.board[i]:
                print("[" + letter + "] ", end ="")
            print()

    def check(self):
        # horizontal row check
        for i in range(0, 3):
            if (self.board[i] == ["X"]*3):
                # print("horizontal X")
                return (True, "X")
            if (self.board[i] == ["O"]*3):
                # print ("horizontal O")
                return (True, "O")
        
        # vertical column check
        for c in range(0, 3):
            if (self.board[0][c] == self.board[1][c] and
                self.board[1][c] == self.board[2][c] and
                self.board[2][c] == "X"):
                # print("vertical X")
                return (True, "X")
            if (self.board[0][c] == self.board[1][c] and
                self.board[1][c] == self.board[2][c] and
                self.board[2][c] == "O"):
                # print("vertical O")
                return (True, "O")
        
        # tl-br diagonal check
        if (self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2] and
            self.board[2][2] == "X"):
            # print("tl-br X")
            return (True, "X")
        if (self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2] and
            self.board[2][2] == "O"):
            # print("tr-bl O")
            return (True, "O")
        
        # tr-bl diagonal check
        if (self.board[0][2] == self.board[1][1] and
            self.board[1][1] == self.board[2][0] and
            self.board[2][0] == "X"):
            # print("tr-bl X")
            return (True, "X")
        
        if (self.board[0][2] == self.board[1][1] and
            self.board[1][1] == self.board[2][0] and
            self.board[2][0] == "O"):
            # print("tr-bl O")
            return (True, "O")
        
        return (False, "n/a")
            

game_board = TicTacToe([[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]])

letter = "O"
while (not (game_board.check()[0])):
    if (letter == "O"):
        letter = "X"
    elif (letter == "X"):
        letter = "O"

    os.system("cls")
    game_board.draw()

    print(letter + "'s turn!")

    # force valid row
    row = input("What row?: ")
    while (not (row.isdigit() and 0 <= int(row) and int(row) < 3)):
        row = input("What row?: ")

    # force valid column
    col = input("What column?: ")
    while not(col.isdigit() and 0 <= int(col) and int(col) < 3):
        col = input("What column?: ")

    # force valid combination when incorrect
    while(not (game_board.board[int(row)][int(col)] == " ")):
        valid_row = False
        valid_col = False
        print("Occupied space! Stop.")

        # force valid row
        row = input("What row?: ")
        while (not (row.isdigit() and 0 <= int(row) and int(row) < 3)):
            row = input("What row?: ")

        # force valid column
        col = input("What column?: ")
        while not(col.isdigit() and 0 <= int(col) and int(col) < 3):
            col = input("What column?: ")

    game_board.board[int(row)][int(col)] = letter

os.system("cls")
game_board.draw()
print(letter + " won!")