print("hello world")
print("This is a TIC TAC TOE game \n \n")
p1 = ' X '
p2 = ' O '

class map:
    def __init__(self):
        self.empty = '  '
        self.p1 = ' X '
        self.p2 = ' O '
        self.grid = [[],[],[]]
        for i in range(3):
            self.grid[0].append(self.empty)
            self.grid[1].append(self.empty)
            self.grid[2].append(self.empty)
            ##self.grid[0].append(self.p1)
            ##self.grid[1].append(self.p1)
            ##self.grid[2].append(self.p1)
        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
    
    def __str__(self):
        return f"{self.grid[0]}\n{self.grid[1]}\n{self.grid[2]}"

    def check_win(self, player):
        for i in range(3):
            if self.grid[0][i] == player:
                self.grid[1].append(self.empty)
                self.grid[2].append(self.empty)
        

    def check_win_horizontal(self, player, row):
        for i in range(3):
            if self.grid[row][i] != player:
                return False
        print("HORIZONTAL: row " + str(row) + " is a winning row" + player + "wins!")
        return True

    def check_win_vertical(self, player, col):
        for i in range(3):
            if self.grid[i][col] != player:
                return False
        print("VERTICAL: col " + str(col) + " is a winning col" + player + "wins!")
        return True
    
    def check_win_diagonal(self, player):
        if self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player:
            print("DIAGONAL(1):" + player + "wins!")
            return True
        
        if self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player:
            print("DIAGONAL(2):" + player + "wins!")
            return True
    
class do_game:
    def __init__(self):
        self.game = map()
        self.p1 = ' '
        self.p2 = ' '
        self.round = -1
        self.end = False
    
    def get_player(self):
        p1 = input('Do you want X or O? ')
        try:
            assert p1 == 'X' or p1 == 'O'
        except ValueError:
            print("Invalid input: Please enter a valid char.")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        if p1 == 'X':
            self.p1 == ' X '
            self.p2 == ' O '
        else:
            self.p1 == ' O '
            self.p2 == ' X '
    
    def get_move(self):
        move = input('Make your move on the 3x3 board i.e.(0,0): ')
        x = int(move[1])
        y = int(move[3])
        assert(self.game.grid[y][x] == '  ')
        print((x, y))
        return (x, y)

    def do_round(self):
        self.round += 1
        x, y = self.get_move()
        if self.round % 2 == 0:
            self.game.grid[y][x] = p1
            print(self.game)
            if self.check_win(p1):
                self.end = True
        elif self.round % 2 == 1:
            self.game.grid[y][x] = p2
            print(self.game)
            if self.check_win(p2):
                self.end = True
        
    
    def check_win(self, player):
        if self.game.check_win_diagonal(player):
            print(player + " wins!")
            return True
        
        for i in range(3):
            if self.game.check_win_horizontal(player, i) or self.game.check_win_vertical(player, i):
                print(player + " wins!")
                return True
        print("no winner yet!")
        return False




t = do_game()

##t.check_win_horizontal(' X ', 1)
##t.check_win_vertical(' X ', 1)
##t.game.check_win_diagonal(' X ')

t.get_player()
while(not t.end):
    t.do_round()