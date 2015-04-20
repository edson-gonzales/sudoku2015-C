"""
This module is in charge of testing the algorithm base class
"""
import unittest
from ...algorithms.algorithm import Algorithm

class TestAlgorithm(unittest.TestCase):

  def test_sudoku_solver_can_be_created_with_no_arguments(self):
    algorithm = Algorithm()
    self.assertIsInstance(algorithm, Algorithm)

  def test_solve_sudoku_is_not_implemented_and_raises_exception(self):
    algorithm = Algorithm()
    test_string = "123"
    try:
      algorithm.solve_sudoku(test_string)
      self.fail("Solve method not implemented in Base Class")
    except NotImplementedError:
      pass

  def test_retrieve_grid_is_not_implemented_and_raises_exception(self):
    algorithm = Algorithm()

    try:
      algorithm.retrieve_grid_basic_format()
      self.fail("Retrieve method not implemented in Base Class")
    except NotImplementedError:
      pass


if __name__ == '__main__':
  unittest.main()