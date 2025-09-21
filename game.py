class Game:
  def __init__(self):
    self.board = [["_" for _ in range(3)] for _ in range(3)]
    self.winner = 0

  def printBoard(self):
    for i in self.board:
      for j in i:
        print([j], end="")
      print("\n")

  def move(self, player):
    row = int(input("Which row: "))
    col = int(input("Which column: "))
    while row >= len(self.board) or col >= len(self.board) or self.board[row][col] != '_':
      print("Invalid tile, please try again.")
      row = int(input("Which row: "))
      col = int(input("Which column: "))
    if player == 1:
      self.board[row][col] = 'O'
    else:
      self.board[row][col] = 'X'



  def checkRow(self, row):
    c = self.board[row][0]
    for i in self.board[row]:
      if i == '_':
        return False
      elif i != c:
        return False
    if c == 'O':
      self.winner = 1
    else:
      self.winner = 2
    return True

  def checkCol(self, col):
    c = self.board[0][col]
    for row in self.board:
      if row[col] == '_':
        return False
      elif row[col] != c:
        return False
    if c == 'O':
      self.winner = 1
    else:
      self.winner = 2
    return True

  def checkDiagOne(self):
    c = self.board[0][0]
    for i in range(len(self.board)):
      if self.board[i][i] == '_' or self.board[i][i] != c:
        return False
    if c == 'O':
      self.winner = 1
    else:
      self.winner = 2
    return True

  def checkDiagTwo(self):
    c = self.board[0][len(self.board) - 1]
    for i in range(len(self.board)):
      if self.board[i][len(self.board) - 1 - i] == '_' or self.board[i][len(self.board) - 1 - i] != c:
        return False
    if c == 'O':
      self.winner = 1
    else:
      self.winner = 2
    return True     

  def checkWinner(self):
    for i in range(len(self.board)):
      self.checkRow(i)
      self.checkCol(i)
    self.checkDiagOne()
    self.checkDiagTwo()
    if self.winner == 0:
      return False
    else:
      return True
    
  def printWinner(self):
    print("Player ", self.winner, " wins the game!")



g = Game()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to TIC-TAC-TOE!")
print("All rows and columns are 0-indexed.")
print("Have fun!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
while not g.checkWinner():
  g.printBoard()
  g.move(1)
  if not g.checkWinner():
    g.printBoard()
    g.move(2)

g.printBoard()
g.printWinner()