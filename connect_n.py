import os
import time

NUM_TO_STR = {
    0: " ",
    1: "x",
    -1: "o",
}

class Connect_N():
    def __init__(self,cols=7,rows=6,connect=4):
        self.player = 1
        self.cols = cols
        self.rows = rows
        self.connect = connect
        self.board = [[0]*cols for _ in range(rows)]
        self.finished = False

    def drop_col(self, col):
        is_full = True
        for i in range(self.rows-1,-1,-1):
            if self.board[i][col] == 0:
                self.board[i][col] = self.player
                self.player *= -1
                is_full = False
                break
            
        return is_full  

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.cols):
            if  i == self.cols - 1:
                print(f"{i+1}")
            else:
                print(f"{i+1} ", end="")
        for i in range(self.rows):
            for j in range(self.cols):
                if j == self.cols - 1:
                    print(f"{NUM_TO_STR[self.board[i][j]]}")
                else:
                    print(f"{NUM_TO_STR[self.board[i][j]]}|", end="")
            print(("__"*self.cols)[:2*self.cols-1])

    def display_player(self):
        print(f"The current player is: player {NUM_TO_STR[self.player]}")

    def play(self):
        self.print_board()

        while(not self.finished):
            print(f"This is connect-{self.connect}, it is a {self.rows}x{self.cols} board")
            self.display_player()
            #TODO boundry check
            col = int(input("What column: "))
            is_full = self.drop_col(col-1)

            if is_full:
                print("The column is full")
                time.sleep(1)

            os.system("cls" if os.name == "nt" else "clear")
            self.print_board()

            winner = self.check_winner()
            tie = self.check_tie()

            if winner:
                print(f"The winner is {NUM_TO_STR[winner]}")
                self.finished = True
            elif tie:
                print("Its a tie")
                self.finished = True


    def check_winner(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:

                    if i + self.connect <= self.rows:
                        win = True
                        for k in range(1,self.connect):
                            if self.board[i][j] != self.board[i+k][j]:
                                win = False
                                break
                        if win: return self.board[i][j]

                    if j + self.connect <= self.cols:
                        win = True
                        for k in range(1,self.connect):
                            if self.board[i][j] != self.board[i][j+k]:
                                win = False
                                break
                        if win: return self.board[i][j]

                    if j + self.connect <= self.cols and i + self.connect <= self.rows:
                        win = True
                        for k in range(1,self.connect):
                            if self.board[i][j] != self.board[i+k][j+k]:
                                win = False
                                break
                        if win: return self.board[i][j]
                    
                    if j + self.connect <= self.cols and i - (self.connect-1) >= 0:
                        win = True
                        for k in range(1,self.connect):
                            if self.board[i][j] != self.board[i-k][j+k]:
                                win = False
                                break
                        if win: return self.board[i][j]
        return 0
    
    def check_tie(self):
        for row in self.board:
            for cell in row:
                if not cell:
                    return False
        return True 
                    
def main():
    game = Connect_N(cols=1,rows=1,connect=2)
    game.play()

main()