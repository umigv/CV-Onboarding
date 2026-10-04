import ticTacToe

def main():
    game = ticTacToe()
    for _ in range(9):
        row = input("Enter row: ")
        col = input("Enter column: ")
        game.round(row,col)
        game.print(game)
        if game.won() == True:
            break
    return 0
