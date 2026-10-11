
class TicTacToe: 
    players = [None for _ in range(2)] # player names
    def __init__(self):
        self.grid = [["#" for _ in range(3)] for _ in range(3)]
        self.active_player = "X"
        self.turn = 0
        print("Tic Tac Toe! You are playing tic tac toe! You are currently player X.")
        
    def round(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position! Use 0, 1, or 2.")
            return False

        if self.grid[row][col] != "#":
            print("This position is already taken!")
            return False
        
        self.grid[row][col] = self.active_player
        return True

    def won(self):
        a = self.active_player
        if((a == self.grid[0][0]) and (a == self.grid[1][0]) and (a == self.grid[2][0])):
            return True
        if((a == self.grid[0][1]) and (a == self.grid[1][1]) and (a == self.grid[2][1])):
            return True
        if((a == self.grid[0][2]) and (a == self.grid[1][2]) and (a == self.grid[2][2])):
            return True
        if((a == self.grid[0][0]) and (a == self.grid[0][1]) and (a == self.grid[0][2])):
            return True
        if((a == self.grid[1][0]) and (a == self.grid[1][1]) and (a == self.grid[1][2])):
            return True
        if((a == self.grid[2][0]) and (a == self.grid[2][1]) and (a == self.grid[2][2])):
            return True
        if((a == self.grid[2][2]) and (a == self.grid[1][1]) and (a == self.grid[0][0])):
            return True
        if((a == self.grid[0][2]) and (a == self.grid[1][1]) and (a == self.grid[2][0])):
            return True
        return False

    def print_board(self):
        continue_game = True
        print(
            f"""
            Your current board:
                {self.grid[0][0]}       |       {self.grid[0][1]}       |       {self.grid[0][2]}
            ------------------------------------------
                {self.grid[1][0]}       |       {self.grid[1][1]}       |       {self.grid[1][2]}
            ------------------------------------------
                {self.grid[2][0]}       |       {self.grid[2][1]}       |       {self.grid[2][2]}
            """
        )
        self.turn += 1
        if self.won():
            print("You've won!")
            continue_game = False
            return continue_game
        elif(self.turn < 8):
            if self.active_player == "X": self.active_player = "O"
            else: self.active_player = "X"
            print(f"Next turn for {self.active_player}! Enter your row, then your column")
            return continue_game
        print("Womp womp, you both lost boo")
        continue_game = False
        return continue_game

    # def game():
    #     game = TicTacToe()
        

if __name__ == "__main__":
    game = TicTacToe()
    for _ in range(9):
        successful_round = False
        while not successful_round:
            try:
                row = int(input("Enter row(0-2): "))
                col = int(input("Enter column(0-2): "))
                successful_round = game.round(row,col)
            except ValueError:
                print("Enter a number!")
    
        
        if game.print_board() == False:
            break