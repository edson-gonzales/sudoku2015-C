"""
This module is going to use the brute force algorithm to solve the sudoku grid
which will be specified here as a string sequence of 81 characters.
"""
import sys
import math
import time
from algorithm import Algorithm
from algorithm import elapsed_time

class BruteForce(Algorithm):
  def __init__(self):
    """Initializes the variables that will be used througout the class.
    number_of_rows:
    Keyword arguments:
      self.number_of_rows -- number of rows that a standard sudoku puzzle has (9)
      self.square_root -- square root of the number of rows. {3}
      self.puzzle -- An array of the 81 integers that compose the puzzle
      self.known_indices -- An array of all the positions of the non-zero values
    """
    self.number_of_rows = 9
    self.square_root = int(math.sqrt(9))
    self.puzzle = []
    self.known_indices = []

  @elapsed_time
  def solve_sudoku(self, grid_basic_format):
    """
    Overrides the solve_sudoku superclass method, for the Brute force algorithm we need
    to visit each cell to fill digits calling the solve_from method, first we visit 
    the "O" first cell with the "1" guess.
    Keyword arguments:
      grid_basic_format -- a long string with 81 digit characters.
    """ 
    self.load_puzzle(grid_basic_format)
    cell = self.solve_from(0, 1)
    while cell is not None:
      cell = self.solve_from(cell[0], cell[1])

  def load_puzzle(self, grid):
    self.puzzle = []
    self.known_indices = []
    rows = []
    for row in grid:
      if row:
        rows.append(row)

    for row_index, row in enumerate(rows):
      if row.isdigit():
        self.puzzle.append(int(row))
        if int(row) != 0:
          self.known_indices.append(row_index)

  def solve_from(self, index, starting_guess):
    """ 
    Method which visits empty cells and start guessing filling numbers and calling
    the valid() method which in turn will be in charge of verifying the correcteness
    of the guess, if the guess is valid it will be added to the puzzle,
    otherwise the puzzle will be reset because the puzzle will not be solvable with
    the wrongly considered valid guesses found until now.
    Keyword arguments:
      index -- index that will track the position where to fill the guesses.
      starting_guess -- value from 1 to 9 that will be validated in each cell.
    """
    if index < 0 or index > len(self.puzzle):
      raise Exception("Invalid puzzle index %s" % (index))

    last_valid_guess_index = None
    found_valid_guess = False
    for i in xrange(index, len(self.puzzle)):
      if i not in self.known_indices:
        found_valid_guess = False
        for guess in xrange(starting_guess, self.number_of_rows + 1):
          if self.valid(i, guess):
            found_valid_guess = True
            last_valid_guess_index = i
            self.puzzle[i] = guess
            break

        starting_guess = 1
        if not found_valid_guess:
          break

    if not found_valid_guess:
      new_index = last_valid_guess_index if last_valid_guess_index is not None else index - 1
      new_starting_guess = self.puzzle[new_index] + 1
      self.reset_puzzle_at(new_index)

      while new_starting_guess > self.number_of_rows or new_index in self.known_indices:
        new_index -= 1
        new_starting_guess = self.puzzle[new_index] + 1
        self.reset_puzzle_at(new_index)

      return (new_index, new_starting_guess)
    else:
      return None

  def reset_puzzle_at(self, index):
    """ Resets the guesses from a certain index because the puzzle will not be solvable with
    the wrongly considered valid guesses found until now.
    Keyword arguments:
      index -- the puzzle will be reset starting from that index specified.
    """
    for i in xrange(index, len(self.puzzle)):
      if i not in self.known_indices:
        self.puzzle[i] = 0

  def valid_for_row(self, index, guess):
    """ Validates that the "guess" filled in an "index" cell is not breaking the puzzle rule
    that establishes that a row should only have one occurrence of numbers from 1 to 9.
    Keyword arguments:
      index -- index that is tracking the position where to fill the guess.
      guess -- value from 1 to 9 that will be validated in this method.
    """
    row_index = int(math.floor(index / self.number_of_rows))
    start = self.number_of_rows * row_index
    finish = start + self.number_of_rows
    for c_index in xrange(start, finish):
      if c_index != index and self.puzzle[c_index] == guess:
        return False
    return True

  def valid_for_column(self, index, guess):
    """ Validates that the "guess" filled in an "index" cell is not breaking the puzzle rule
    that establishes that a column should only have one occurrence of numbers from 1 to 9.
    Keyword arguments:
      index -- index that is tracking the position where to fill the guess.
      guess -- value from 1 to 9 that will be validated in this method.
    """
    col_index = index % self.number_of_rows
    for cell in xrange(0, self.number_of_rows):
      cell_index = col_index + (self.number_of_rows * cell)
      if cell_index != index and self.puzzle[cell_index] == guess:
        return False
    return True

  def valid_for_block(self, index, guess):
    """ Validates that the "guess" filled in an "index" cell is not breaking the puzzle rule
    that establishes that a block should only have one occurrence of numbers from 1 to 9.
    Keyword arguments:
      index -- index that is tracking the position where to fill the guess.
      guess -- value from 1 to 9 that will be validated in this method.
    """
    row_index = int(math.floor(index / self.number_of_rows))
    col_index = index % self.number_of_rows

    block_row = int(math.floor(row_index / self.square_root))
    block_col = int(math.floor(col_index / self.square_root))

    row_start = block_row * self.square_root
    row_end = row_start + self.square_root - 1
    col_start = block_col * self.square_root
    col_end = col_start + self.square_root - 1

    for cell in xrange(row_start, row_end + 1):
      for visit in xrange(col_start, col_end + 1):
        i = visit + (cell * self.number_of_rows)
        if self.puzzle[i] == guess:
          return False

    return True

  def valid(self, index, guess):
    """ Evaluates the 3 validation types required to define a valid guess to solve the puzzle.
    Keyword arguments:
      index -- index that is tracking the position where to fill the guess.
      guess -- value from 1 to 9 that will be validated in this method.

    """
    return self.valid_for_row(index, guess) and self.valid_for_column(index, guess) \
    and self.valid_for_block(index, guess)

  def retrieve_grid_basic_format(self):
    """
    Overrides the retrieve_grid_basic_format superclass method, for this algorithm is required
    to convert the solution stored in an array of 81 integers to a string of 81 characters
    """ 
    return ''.join(str(v) for v in self.puzzle)



