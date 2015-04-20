""" This class will be in charge of filling a 9x9 grid with digits """

class SudokuGrid(object):

  def __init__(self):
    """  Throughout this program we have:
    r is a row,    e.g. 'A'
    c is a column, e.g. '3'
    s is a square, e.g. 'A3'
    d is a digit,  e.g. '9'
    u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
    grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
    values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}
    """

    self.digits = '123456789'
    self.rows = 'ABCDEFGHI'
    self.cols = self.digits
    self.squares = self.cross(self.rows, self.cols)
    self.unitlist = ([self.cross(self.rows, c) for c in self.cols] + \
      [self.cross(r, self.cols) for r in self.rows] + \
      [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
    self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.squares)
    self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)
    self.grid_values = None
    self.string_grid = None


  def cross(self, A, B):
    """Cross product of elements in A and elements in B.
    Keyword arguments:
      A -- an array of letters [A, B, C...]
      B -- an array of digits [1, 2, 3...]
    """
    return [a+b for a in A for b in B]

  def load_grid_values(self, string_grid):
    """Converts a grid (string basic format) into a dict of {square: char}
    with '0' or '.' for empties.
    Keyword arguments:
      string_grid -- an array of 81 characters
    """
    self.string_grid = string_grid
    chars = [c for c in string_grid if c in self.digits or c in '0.']
    # assert len(chars) == 81
    self.grid_values = dict(zip(self.squares, chars))

  def display_2D_grid(self):
    """Display the puzzle values as a 2-D grid."""
    outcome = ""
    width = 1+max(len(self.grid_values[s]) for s in self.squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in self.rows:
      outcome += ''.join(self.grid_values[r+c].center(width) + \
         ('|' if c in '36' else '')for c in self.cols) + '\n'
      if r in 'CF':
        outcome += line + '\n'
    return outcome

  def display_simple_grid(self):
    """Display the puzzle values as a simple grid."""
    outcome = ""
    outcome += "".join(['\n' + str(c) if i % 9 == 0 else str(c) \
      for i, c in enumerate(self.string_grid)])
    outcome += "\n"
    return outcome






    










