from copy import deepcopy
from dfs_algorithm import Node

class Sudoku(Node):
  """
    This class used to represent the sudoku board
    ...

    Attributes
    ----------
    puzzle : List
        represent the puzzle  
    rows : Integer, optional
        represents number of rows
    cols : Integer, optional
        represents the number of columns
  

    Methods
    -------
    __eq__(self, other)
        Determines if the current sudoku is the same with the other 
    
    check_row(self, row, value)
        Checks if the value is unique in the specific row

    check_col(self, col, value):
        Checks if the value is unique in the specific column
    
    check_sqaure(self, row, col, value)
        Checks if the value is unique in the specific square
    
    find_first_epty_slot(self)
        Finds the first slot in the puzzle with value 0, which means that the slot in empty

    extend_node(self)
        Extends the current node, creating a new instance of Sudoku for each valid number

    is_the_solution(self)
        Checks if the current node is the solution

    __str__(self)
        Returns the sudoku board in order to be printed properly
    """
  def __init__(self, puzzle, rows=9, cols=9):
    self.puzzle = puzzle
    self.rows = rows
    self.cols = cols

  
  def __eq__(self, other):   
    """
      Check if the current puzzle is equal with the other puzzle.

      Parameters
      ----------
      Other : Sudoku
          The other sudoku puzzle

      Returns
      -------
      Boolean
        True: if both puzzles are the same
        False: If puzzles are different
    """ 
    if isinstance(other, Sudoku):
      return self.puzzle == other.puzzle
    return self.puzzle == other

  
  def check_row(self, row, value):
    """
      Checks if the value is unique in the specific row

      Parameters
      ----------
      row : Integer
          The number of row 
      value: Integer
          The possible number for this row

      Returns
      -------
      Boolean
        True: if the value is valid in the row
        False: If the value is not valid
    """
    for col in range(self.cols):
      if value == self.puzzle[row][col]:
        return False
    return True
  

  def check_col(self, col, value):
    """
      Checks if the value is unique in the specific column

      Parameters
      ----------
      col : Integer
          The number of column 
      value: Integer
          The possible number for this row
      
      Returns
      -------
      Boolean
        True: if the value is valid in the column
        False: If the value is not valid
    """
    for row in range(self.rows):
      if value == self.puzzle[row][col]:
        return False
    return True
  

  def check_sqaure(self, row, col, value):
    """
      Checks if the value is unique in the specific square
      First caluclate the square and the checks if exists number
      with the same value in this square

      Parameters
      ----------
      row : Integer
          The number of row 
      col : Integer
          The number of column 
      value: Integer
          The possible number for this row
      
      Returns
      -------
      Boolean
        True: if the value is valid 
        False: If the value is not valid
    """
    square_row_start = (row // 3) * 3
    square_col_start = (col // 3) * 3

    for row in range(square_row_start, square_row_start + 3):
      for col in range(square_col_start, square_col_start + 3):
        if self.puzzle[row][col] == value:
          return False
    return True
  

  def find_first_epty_slot(self):
    """
     Find the first slot in the puzzle with value 0, which means that the slot in empty

      Returns
      -------
      Integer, Integer
        row: the number of row of the first empty slot
        col: the number of col of the first empty slot
    """
    for row in range(self.cols):
      for col in range(self.rows):
        if self.puzzle[row][col] == 0:
          return row, col


  def extend_node(self):
    """
     Extends the current node, creating a new instance of Sudoku for each valid number

      Returns
      -------
      List
        List with all valid new nodes
    """
    row, col = self.find_first_epty_slot()
    new_puzzles = []
    for number in range(1, 9+1):
      if self.check_row(row, number) and self.check_col(col, number) and self.check_sqaure(row, col, number):
        new_puzzle = deepcopy(self.puzzle)
        new_puzzle[row][col] = number
        new_puzzles.append(Sudoku(new_puzzle))
    return new_puzzles

  

  def is_the_solution(self):
    """
     Checks if the current node is the solution

      Returns
      -------
      Boolean
        True: if the puzzle has not empty slots
        False: if puzzle has empty slots
    """
    for row in range(self.rows):
      for col in range(self.cols):
        if self.puzzle[row][col] == 0:
          return False
    return True

  
  def __str__(self):
    """
     Returns the sudoku board in order to be printed properly

      Returns
      -------
      str
        the board of the sudoku
    """
    sudoku = ""
    for row in range(self.rows):
      for col in range(self.cols):
        sudoku += f"{self.puzzle[row][col]} "
      sudoku += "\n"
    return sudoku



  
