""" This class will be in charge of generating a random Sudoku Puzzle using a Dictionary
provided by the SudokuGrid Module.
"""
import random
from sudoku_grid import SudokuGrid

class SudokuBuilder(object):

  def __init__(self, visible_numbers):
    """ Initializes a Grid without digits generated yet
    Keyword arguments:
    grid -- module that is able to build a dictionary of positions and values.
    visible_numbers -- quantity of numbers that will be filled in the puzzle, the rest
    of them will be zeros or empty spaces in UI/Command Line Interface
    """
    self.grid = SudokuGrid()
    self.visible_numbers = visible_numbers

  def build_random_grid(self):
    """Build a random puzzle with N or more assignments. Restart on contradictions.
    Note the resulting puzzle is not guaranteed to be solvable, but empirically
    about 99.8% of them are solvable. Some have multiple solutions.
    Returned arguments:
      A long string with 81 characters where zeros that represent empty cells
    """
    values = dict((s_index, self.grid.digits) for s_index in self.grid.squares)
    for s_index in self.shuffled(self.grid.squares):
      if not self.assign(values, s_index, random.choice(values[s_index])):
        break
      ds_index = [values[s_index] for s_index in self.grid.squares if len(values[s_index]) == 1]
      if len(ds_index) >= self.visible_numbers and len(set(ds_index)) >= 8:
        return ''.join(values[s_index] if len(values[s_index]) == 1 else '0' for s_index in self.grid.squares)
    return self.build_random_grid()

  def shuffled(self, seq):
    """Return a randomly shuffled copy of the input sequence.
    Keyword arguments:
      seq -- An array of squares. (E.g. [A1, A2, ...])
    """
    seq = list(seq)
    random.shuffle(seq)
    return seq

  def assign(self, values, s_index, digit):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected.
    Keyword arguments:
      values --  dict of {square: char} to be resolved
      s_index -- position in the grid
      digit -- number to fill it
    """
    other_values = values[s_index].replace(digit, '')
    if all(self.eliminate(values, s_index, d2_index) for d2_index in other_values):
      return values
    else:
      return False

  def eliminate(self, values, s_index, digit):
    """Eliminate digit from values[s_index]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected.
    Keyword arguments:
      values --  dict of {square: char} to be resolved
      s_index -- position in the grid
      digit -- number to fill it
    """
    if digit not in values[s_index]:
      return values ## Already eliminated
    values[s_index] = values[s_index].replace(digit, '')
    ## (1) If a square s is reduced to one value d2_index, then eliminate d2_index from the peers.
    if len(values[s_index]) == 0:
      return False ## Contradiction: removed last value
    elif len(values[s_index]) == 1:
      d2_index = values[s_index]
      if not all(self.eliminate(values, s2, d2_index) for s2 in self.grid.peers[s_index]):
        return False
    ## (2) If a unit u_index is reduced to only one place for a value digit, then put it there.
    for u_index in self.grid.units[s_index]:
      dplaces = [s_index for s_index in u_index if digit in values[s_index]]
      if len(dplaces) == 0:
        return False ## Contradiction: no place for this value
      elif len(dplaces) == 1:
        if not self.assign(values, dplaces[0], digit):
          return False
    return values


    








