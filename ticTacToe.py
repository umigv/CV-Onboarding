
class TicTacToe:
    global grid
    global active_player 
    global turn
    players = [None for _ in range(2)] # player names
    def __init__():
        grid = [[None for _ in range(3)] for _ in range(3)]
        active_player = "X"
        turn = 0
        print("Tic Tac Toe! You are playing tic tac toe! You are currently player X.")
        
        
    def round(row, col):
        grid[row][col] = active_player

    def won():
        a = active_player
        if((a == grid[0][0]) and (a == grid[1][0]) and (a == grid[2][0])):
            return True
        if((a == grid[0][1]) and (a == grid[1][1]) and (a == grid[2][1])):
            return True
        if((a == grid[0][2]) and (a == grid[1][2]) and (a == grid[2][2])):
            return True
        if((a == grid[0][0]) and (a == grid[0][1]) and (a == grid[0][2])):
            return True
        if((a == grid[1][0]) and (a == grid[1][1]) and (a == grid[1][2])):
            return True
        if((a == grid[2][0]) and (a == grid[2][1]) and (a == grid[2][2])):
            return True
        if((a == grid[2][2]) and (a == grid[1][1]) and (a == grid[0][0])):
            return True
        if((a == grid[0][2]) and (a == grid[1][1]) and (a == grid[2][0])):
            return True
        return False

    def print(self):
        print(
            """
            Your current board:
            {grid[0][0]} | {grid[0][1]} | {grid[0][2]}
            ------------------------------------------
            {grid[1][0]} | {grid[1][1]} | {grid[1][2]}
            ------------------------------------------
            {grid[2][0]} | {grid[2][1]} | {grid[2][2]}
            """
        )
        turn += 1
        if self.won():
            print("You've won!")
        elif(turn != 8):
            print("Next turn! Enter your row, then your column")
        else:
            print("Womp womp, you lost boo")

