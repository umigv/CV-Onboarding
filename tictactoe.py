class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.turn = 'X'


    def start(self):
        while True:
            print(f'{self.turn}\'s turn, enter row: ', end = '')
            i = int(input())
            print(f'.      enter column: ', end = '')
            j = int(input())

            status = self.play(i, j)
            self.display_board()

            if status == 1:
                print(f'{self.turn} wins!')
                return
            
            if status == 2:
                print('Tie!')
                return
            
            if status != -1:
                self.turn = 'X' if self.turn == 'O' else 'O'


    def display_board(self):
        print()
        print(f'.     {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}')
        print(f'.     - | - | - ')
        print(f'      {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}')
        print(f'      - | - | - ')
        print(f'      {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}')
        print()


    def play(self, i, j):
        if self.board[i][j] != ' ':
            print('Invalid move, try again')
            return -1

        self.board[i][j] = self.turn

        return self.check_win()
    
    
    def check_win(self):
        
        if ((self.board[0][0] == self.board[0][1] == self.board[0][2]) and self.board[0][0] != ' ') \
            or ((self.board[1][0] == self.board[1][1] == self.board[1][2]) and self.board[1][0] != ' ') \
            or ((self.board[2][0] == self.board[2][1] == self.board[2][2]) and self.board[2][0] != ' ') \
            or ((self.board[0][0] == self.board[1][0] == self.board[2][0]) and self.board[0][0] != ' ') \
            or ((self.board[0][1] == self.board[1][1] == self.board[2][1]) and self.board[0][1] != ' ') \
            or ((self.board[0][2] == self.board[1][2] == self.board[2][2]) and self.board[0][2] != ' ') \
            or ((self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != ' ') \
            or ((self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != ' '):
            return 1
        
        if self.board[0][0] != ' ' and self.board[0][1] != ' ' and self.board[0][2] != ' ' and \
           self.board[1][0] != ' ' and self.board[1][1] != ' ' and self.board[1][2] != ' '  and \
           self.board[2][0] != ' ' and self.board[2][1] != ' ' and self.board[2][2] != ' ':
            return 2
        
        return 0
        

                

game = TicTacToe()

game.start()