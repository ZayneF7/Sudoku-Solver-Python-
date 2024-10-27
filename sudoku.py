# Author: Zayne Foster
# Date: 7/22/2024
# sudoku.py -- Recursive sudoku solver

# Sudoku board is a matrix represented by a list containing 9 lists of numbers
# 0 represents an empty slot
my_board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Prints sudoku board
def print_board(board):
  for i in range(len(board)):
    if (i % 3 == 0) and (i != 0): # Prints horizontal divider after every 3 rows
      print("- - - - - - - - - - -")

    for j in range(len(board)):
      if (j % 3 == 0) and (j != 0): # Prints vertical divider after every 3 columns
        print("| ", end = "")

      if (j == 8):
        print(board[i][j]) # Produces new line after the 9th index of each row
      else:
        print(f'{board[i][j]} ', end = "") # Remains on the same line for entries other than the 9th index

# Returns the position of the first found empty square in the board
def find_empty(board):
  for i in range(len(board)):
    for j in range(len(board)):
      if (board[i][j] == 0):
        return (i, j) #(row, column)
  
  return None
      
# Checks if the number in a given position appears anywhere else in its row
def check_row(board, num, pos):
  for i in range(len(board)): # i = column number
    if (board[pos[0]][i] == num) and (pos[1] != i):
      return False
  
  return True

# Checks if the number in a given position appears anywhere else in its column
def check_col(board, num, pos):
  for i in range(len(board)):
    if (board[i][pos[1]] == num) and (pos[0] != i):
      return False
  
  return True

# Checks if the number in a given position appears anywhere else in its designated 3x3 box
def check_box(board, num, pos):
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3): 
      if (board[i][j] == num) and (pos != (i, j)):
        return False
  
  return True
  

# Checks if the board adheres to the rules of Sudoku
# board -- provided Sudoku board
# num -- the number that the program is attempting to add to the board
# pos -- current position on the board
def valid_board(board, num, pos):
  return check_row(board, num, pos) and check_col(board, num, pos) and check_box(board, num, pos)

# Algorithm that solves sudoku board   
def solve(board):
  position = find_empty(board)

  if not position: # If an empty slot was not found, the board must be complete (base case)
    return True
  else:
    row, col = position

  for num in range(1, 10): # Try inserting numbers 1-9 into position
    if valid_board(board, num, position):
      board[row][col] = num # If a given num at the given position produces a valid board, insert that num into the once empty slot
      
      if solve(board): # Solve for the newly produced board (recursion)
        return True # If the board produced in the following iteration is valid, then it must be valid for this current iteration
      
      board[row][col] = 0 # Resets the current position to 0 (empty) if a valid board was not produced on the following iteration
      
  return False # Signifies that the board in its current state is not valid


print_board(my_board)
print("\n\n")

solve(my_board)

print_board(my_board)