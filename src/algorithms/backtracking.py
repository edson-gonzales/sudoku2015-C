"""
This module is going to use the backtracking algorithm to resolve 
the sudoku grid which will be specified here as a sequence of 81 characters.
"""
from algorithm import Algorithm
from algorithm import elapsed_time

class Backtracking(Algorithm):
  def __init__(self):
    """
    Initializes the variables that will be used througout the class.
    Keyword arguments:
      self.grid -- the input value that is a string of 81 characters
    """
    self.grid = None

  @elapsed_time
  def solve_sudoku(self, grid_basic_format):
    """
    Load the puzzle and solve it.
    Keyword arguments:
      grid_basic_format -- a  string with 81 digit characters.
    """ 
    self.load_puzzle(grid_basic_format)
    self.solve_backtracking()

  def load_puzzle(self, grid_basic_format):
    """
    Receives a string with 81 characters and transforms it to a list of list
    Keyword arguments:
      grid_basic_format -- a  string with 81 digit characters.
      dimension -- an integer that represents the numbers that will contain each list
    """
    dimension = 9
    list_of_numbers = [int(n) for n in grid_basic_format]
    list_of_list = [[0] * dimension] * dimension
    for row in range(dimension):
      list_of_list[row] = list_of_numbers[row * dimension : (row + 1) * dimension]
    self.grid = list_of_list

  def find_next_cell_to_fill(self, i, j):
    """
    Return the cell that is unfilled, the cell that contains 0
    """
    for x in range(i,9):
      for y in range(j,9):
        if self.grid[x][y] == 0:
          return x, y
    for x in range(0,9):
      for y in range(0,9):
        if self.grid[x][y] == 0:
          return x, y
    return -1, -1

  def is_valid(self, i, j, e):
    """
    Validates that the cell is not breaking the rule that establishes that a row 
    should only have one occurrence of numbers from 1 to 9.
      It finds the top left x,y co-ordinates of the section containing the i,j cell
    """
    row_ok = all([e != self.grid[i][x] for x in range(9)])
    if row_ok:
      column_ok = all([e != self.grid[x][j] for x in range(9)])
      if column_ok:
        sec_topx, sec_topy = 3 *(i/3), 3 *(j/3)
        for x in range(sec_topx, sec_topx+3):
          for y in range(sec_topy, sec_topy+3):
            if self.grid[x][y] == e:
              return False
        return True
    return False

  def solve_backtracking(self, i=0, j=0):
    """
    Method that visit the empty cells (contains 0) and solve a sudoku game
    validating that an entered digit is valid.
    """
    i, j = self.find_next_cell_to_fill(i, j)
    if i == -1:
      return True
    for e in range(1,10):
      if self.is_valid(i, j, e):
        self.grid[i][j] = e
        if self.solve_backtracking(i, j):
          return True
        self.grid[i][j] = 0
    return False



  def retrieve_grid_basic_format(self):
    """
    Overrides the retrieve_grid_basic_format superclass method, for this algorithm is required
      to convert the solution stored in a list of lists of 81 integers to a string of 81 characters
    """
    outcome = ""
    for first_list in self.grid:
      for number in first_list:
        outcome += ''.join(str(number))
    return outcome

