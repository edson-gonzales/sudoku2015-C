"""
This module is going to use the brute force algorithm to solve the sudoku grid
which will be specified here as a string sequence of 81 characters.
"""
import sys
import math
import time
from algorithm import Algorithm
from algorithm import elapsed_time
from ..game.sudoku_grid import SudokuGrid

class PeterNorvig(Algorithm):
  """ Initializes a Gridwithout digits generated yet
  Keyword arguments:
  sudoku_grid -- module that is able to build a dictionary of positions and values.
  string_grid -- the input value that is a string of 84 characters where zero represents empty
  grid_resolved -- the input value that is a string of 84 characters without zeros
  """
  def __init__(self):
    self.sudoku_grid = SudokuGrid()
    self.string_grid = None
    self.grid_resolved = None


  @elapsed_time
  def solve_sudoku(self, grid_basic_format):
    """ Initializes a Grid without digits generated yet
    Keyword arguments:
    grid_basic_format -- string of 84 characters where zero represents empty cells
    """
    self.sudoku_grid.load_grid_values(grid_basic_format)
    self.grid_resolved = self.search(self.parse_grid(grid_basic_format))


  def search(self, values):
    """Using depth-first search and propagation, try all possible values.
    Keyword arguments:
    values -- dict of possible values, {square: digits}
    """
    if values is False:
        return False ## Failed earlier
    if all(len(values[square]) == 1 for square in self.sudoku_grid.squares):
        return values ## Solved!
    ## Chose the unfilled square square with the fewest possibilities
    number,square = min((len(values[square]), square) for square in self.sudoku_grid.squares if len(values[square]) > 1)
    return self.some(self.search(self.assign(values.copy(), square, digit)) for digit in values[square])

  def some(self, squares):
    """Return if elements are contained in squares array.
    Keyword arguments:
      squares -- An array of squares. (E.g. [A1, A2, ...])
    """
    for element in squares:
        if element: return element
    return False

  def parse_grid(self, grid_basic_format):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected.
    Keyword arguments:
      grid_basic_format -- A long string with 81 characters where zeros that represent empty cells
    """
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((square, self.sudoku_grid.digits) for square in self.sudoku_grid.squares)
    for square, digit in self.grid_values(grid_basic_format).items():
        if digit in self.sudoku_grid.digits and not self.assign(values, square, digit):
            return False ## (Fail if we can't assign digit to square square.)
    return values

  def grid_values(self, grid_basic_format):
    """ Convert grid into a dict of {square: char} with '0' or '.' for empties.
    Keyword arguments:
      grid_basic_format -- A long string with 81 characters where zeros that represent empty cells
    Returned parameter:
      dictionary -- dict of {square: char} e.g {'A1': '0', 'A2': '1', etc...}
    """
    chars = [char for char in grid_basic_format if char in self.sudoku_grid.digits or char in '0.']
    dictionary = dict(zip(self.sudoku_grid.squares, chars))
    return dictionary

  def assign(self, values, s_index, digit):
    """Eliminate all the other values (except digit) from values[s_index] and propagate.
    Return values, except return False if a contradiction is detected.
    Keyword arguments:
      values --  dict of {square: char} to be resolved
      s_index -- position in the grid
      digit -- number to fill it
    """
    other_values = values[s_index].replace(digit, '')
    if all(self.eliminate(values, s_index, second_digit) for second_digit in other_values):
        return values
    else:
        return False

  def eliminate(self, values, s_index, digit):
    """Eliminate digit from values[s_index]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if digit not in values[s_index]:
        return values ## Already eliminated
    values[s_index] = values[s_index].replace(digit, '')
    ## (1) If a square s_index is reduced to one value second_digit, then eliminate second_digit from the peers.
    if len(values[s_index]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s_index]) == 1:
        second_digit = values[s_index]
        if not all(self.eliminate(values, second_square, second_digit) \
        for second_square in self.sudoku_grid.peers[s_index]):
            return False
    ## (2) If a unit unit is reduced to only one place for a value digit, then put it there.
    for unit in self.sudoku_grid.units[s_index]:
        dplaces = [s_index for s_index in unit if digit in values[s_index]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # digit can only be in one place in unit; assign it there
            if not self.assign(values, dplaces[0], digit): return False
    return values

  def retrieve_grid_basic_format(self):
    outcome = ""
    for row in self.sudoku_grid.rows:
        outcome += ''.join(self.grid_resolved[row+char]+('' if char in '36' else '')\
          for char in self.sudoku_grid.cols)
    return outcome




