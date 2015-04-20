"""
This module is the Algorithm base class created just for generalize the solution process, and
have generic methods that will be implemented by the classes who inherited this base class.
"""
import time

class Algorithm(object):

  def solve_sudoku(self, grid_basic_format):
    """ Generic method that needs to be implemented in the classes who inherit the
    Algorithm object"""
    raise NotImplementedError("Solve sudoku method not implemented in Base Class")

  def retrieve_grid_basic_format(self):
    """ Generic method that needs to be implemented in the classes who inherit the
    Algorithm object, it should return a long string with 81 characters where zeros
    represent empty values. (E.g. "0205089000781300....")
    """
    raise NotImplementedError("Retrieve method not implemented in Base Class")

def elapsed_time(func):
  """ decorator for solve_sudoku method in charge of tracking the puzzle resolution time."""
  def wrapper(*arg):
    # before
    start_time = time.clock()
    res = func(*arg)
    # after
    end_time = time.clock()
    solved_time = end_time - start_time
    print "Sudoku Puzzle was solved in:  %2.4f sec" % (solved_time)
    return res
  return wrapper
