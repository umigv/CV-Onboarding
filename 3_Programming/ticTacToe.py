class TicTacToe():
    def __init__(self):
        self.grid = [["_" for x in range(3)] for x in range(3)]
        self.player1 = input("Enter Player 1 Name (X): ")
        self.player2 = input("Enter Player 2 Name (O): ")
        self.currentPlayer = self.player2
        self.isWinner = False
        self.winner = ""

    def displayBoard(self):
        for row in self.grid:
            for col in row:
                print([col], end="")
            print("\n")

    def updateLocation(self, row, col, symbol):
        if row > 2 or col > 2:
            print("Invalid row/col. Try again.")
            return False
        if (self.grid[row][col] == "_"):
            self.grid[row][col] = symbol
            self.displayBoard()
            return True
        else:
            print("Spot Already Taken. Pick Another Spot.")
            return False


    def takeTurn(self):
        if (self.currentPlayer == self.player1):
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

        if (self.currentPlayer == self.player1):
            if(self.checkTie()): return
            row = int(input("Player 1 Enter Row: "))
            col = int(input("Player 1 Enter Col: "))
            while self.updateLocation(row, col, "X") == False:
                row = int(input("Player 1 Enter Row: "))
                col = int(input("Player 1 Enter Col: "))
        else: 
            if(self.checkTie()): return
            row = int(input("Player 2 Enter Row: "))
            col = int(input("Player 2 Enter Col: "))
            while self.updateLocation(row, col, "O") == False:
                row = int(input("Player 2 Enter Row: "))
                col = int(input("Player 2 Enter Col: "))
                

    def checkWinner(self):
        if (self.isWinner): return 
        # rows
        for row in self.grid:
            if all(cell == "X" for cell in row):
                self.isWinner = True
                self.winner = self.player1
            if all(cell == "O" for cell in row):
                self.isWinner = True
                self.winner = self.player2

        # cols
        for c in range(3):
            if all(self.grid[r][c] == "X"  for r in range(3)):
                self.isWinner = True
                self.winner = self.player1
            if all(self.grid[r][c] == "O"  for r in range(3)):
                self.isWinner = True
                self.winner = self.player2

        # diagonals
        if all(self.grid[i][i] == "X"  for i in range(3)):
            self.isWinner = True
            self.winner = self.player1
        if all(self.grid[i][2 - i] == "O"  for i in range(3)):
            self.isWinner = True
            self.winner = self.player2
    
        if self.isWinner:
            print(self.winner + " wins the game!")
        return False
    
    def checkTie(self):
        for row in range(3):
            for col in range(3):
                if ((self.grid[row][col] == "_")):
                    return False
        print("It's a tie!")
        self.isWinner = True
        return True

    def runGame(self):
        while(self.isWinner == False):
            self.takeTurn()
            self.checkWinner()
              
    
game = TicTacToe()
game.displayBoard()
game.runGame()