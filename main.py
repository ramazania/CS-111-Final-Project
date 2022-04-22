#CS 201 Final Project: Connect4 Game
#Project Submitters: Doug and Ali 

from graphics import *
#Creates a welcome screen
win = GraphWin("My fancy window", 800, 800)
message = Text(Point(400,300), "Welcome to the Connect4 Game!")
message.draw(win)
message.setSize(24)


import random
#Class Board in order to make an instance of game board.
class Board:
  def __init__(self):
    self.makeBoard()
  
  def makeBoard(self):
    self.board = [['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-'], ['-', '-', '-','-', '-', '-','-']]
    return self.board
    
  def drawBoard(self):
    print(' '.join(self.board[0][0:7]))
    print(' '.join(self.board[1][0:7]))
    print(' '.join(self.board[2][0:7]))
    print(' '.join(self.board[3][0:7]))
    print(' '.join(self.board[4][0:7]))
    print(' '.join(self.board[5][0:7]))
    print()
    return self.board
    
  
#This function takes a user input to start the game.
def userTurn(board):
  while True:
    userCol = int(input("Choose a column(0-6): "))
    print()
    if board.board[5][userCol] != "X" and board.board[5][userCol] != "O":
      board.board[5][userCol] = "X"
      break;
    elif board.board[4][userCol] != "X" and board.board[4][userCol] != "O":
      board.board[4][userCol] = "X"
      break;
    elif board.board[3][userCol] != "X" and board.board[3][userCol] != "O":
      board.board[3][userCol] = "X"
      break;
    elif board.board[2][userCol] != "X" and board.board[2][userCol] != "O":
      board.board[2][userCol] = "X"
      break;
    elif board.board[1][userCol] != "X" and board.board[1][userCol] != "O":
      board.board[1][userCol] = "X"
      break;
    elif board.board[0][userCol] != "X" and board.board[0][userCol] != "O":
      board.board[0][userCol] = "X"
      break;
    else:
      print("out of range!")
      break;


# This function takes a random column from the computer and places it on the gameboard.
def aiTurn(board):
  print('AI goes:')
  print()
  while True:
    aiCol = random.randint(0, 6)
    if board.board[5][aiCol] != "X" and board.board[5][aiCol] != "O":
      board.board[5][aiCol] = "O"
      break;
    elif board.board[4][aiCol] != "X" and board.board[4][aiCol] != "O":
      board.board[4][aiCol] = "O"
      break;
    elif board.board[3][aiCol] != "X" and board.board[3][aiCol] != "O":
      board.board[3][aiCol] = "O"
      break;
    elif board.board[2][aiCol] != "X" and board.board[2][aiCol] != "O":
      board.board[2][aiCol] = "O"
      break;
    elif board.board[1][aiCol] != "X" and board.board[1][aiCol] != "O":
      board.board[1][aiCol] = "O"
      break;
    elif board.board[0][aiCol] != "X" and board.board[0][aiCol] != "O":
      board.board[0][aiCol] = "O"
      break;
  

def getWinner(board):
  #Checking for horizontal win
  for c in range (4):
    for r in range(6):
      if  board.board[r][c] == "X" and board.board[r][c+1] == "X" and board.board[r][c+2] == "X" and board.board[r][c+3] == "X":
        return board.board[r][c]
      elif board.board[r][c] == "O" and board.board[r][c+1] == "O" and board.board[r][c+2] == "O" and board.board[r][c+3] == "O":
        return board.board[r][c]

  #Checking for vertical win
  for c in range (7):
    for r in range(3):
      if  board.board[r][c] == "X" and board.board[r+1][c] == "X" and board.board[r+2][c] == "X" and board.board[r+3][c] == "X":
        return board.board[r][c]
      elif  board.board[r][c] == "O" and board.board[r+1][c] == "O" and board.board[r+2][c] == "O" and board.board[r+3][c] == "O":
        return board.board[r][c]

  #Checking for negative diagonal win 
  for c in range (4):
    for r in range(3):
      if  board.board[r][c] == "X" and board.board[r+1][c+1] == "X" and board.board[r+2][c+2] == "X" and board.board[r+3][c+3] == "X":
        return board.board[r][c]
      elif  board.board[r][c] == "O" and board.board[r+1][c+1] == "O" and board.board[r+2][c+2] == "O" and board.board[r+3][c+3] == "O":
        return board.board[r][c]
        
  #Checking for positive diagonal win 
  for c in range (4):
    for r in range(2,6):
      if  board.board[r][c] == "X" and board.board[r-1][c+1] == "X" and board.board[r-2][c+2] == "X" and board.board[r-3][c+3] == "X":
        return board.board[r][c]
      elif  board.board[r][c] == "O" and board.board[r-1][c+1] == "O" and board.board[r-2][c+2] == "O" and board.board[r-3][c+3] == "O":
        return board.board[r][c]

  #Checking for draw
  dashIn = False #keep game going until true
  for r in range(len(board.board)) : 
    for c in range(len(board.board[r])) :
      if board.board[r][c] == '-' : #if dash anywhere in the board
        dashIn = True
  if dashIn == False : #if no dashes
    return "Draw"
  return None #keep game running if no win, loss, or draw




def main():
  # Set up and draw the empty board
  board = Board()
  board.drawBoard()

  # Keep taking turns until someone wins or draw
  while getWinner(board) == None:
    # User goes first
    userTurn(board)
    board.drawBoard()

    # If user doesn't win, give the AI a shot
    if getWinner(board) == None:
      aiTurn(board)
      board.drawBoard()

   # Once the game is over, print the winner
    winner = getWinner(board)
    if winner == "X":
      print('Congratulations--you win!')
    elif winner == 'O':
      print('The computer wins! Better luck next time.')
    elif winner == "Draw" :
      print('It\'s a draw!')

main()