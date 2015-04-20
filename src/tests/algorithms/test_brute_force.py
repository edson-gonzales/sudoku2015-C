"""
This module is in charge of testing the algorithm base class
"""
import unittest
from ...algorithms.algorithm import Algorithm
from ...algorithms.brute_force import BruteForce

class TestBruteForce(unittest.TestCase):

  def test_sudoku_solver_can_be_created_with_no_arguments(self):
    force = BruteForce()
    self.assertIsInstance(force, BruteForce)

  def test_puzzle_can_be_loaded(self):
    string_grid = "10305"
    expected_result = [1, 0, 3, 0, 5]
    force = BruteForce()
    force.load_puzzle(string_grid)
    actual_result = force.puzzle
    self.assertEquals(expected_result, actual_result)

  def test_puzzle_is_solved_correctly(self):
    string = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
    force = BruteForce()
    force.solve_sudoku(string)

    expected_result = "483921657967345821251876493548132976729564138136798245372689514814253769695417382"
    actual_result =force.retrieve_grid_basic_format()
    self.assertEquals(expected_result, actual_result)

  def test_puzzle_can_be_formatted_as_valid_output(self):
    expected_result = "10305"
    force = BruteForce()
    force.puzzle = [1, 0, 3, 0, 5]
    actual_result = force.retrieve_grid_basic_format()
    self.assertEquals(expected_result, actual_result)

  def test_validation_of_row_for_a_guess(self):
    force = BruteForce()
    force.puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1]
    guess = 9
    index = 8
    self.assertTrue(force.valid_for_row(index, guess))

  def test_validation_of_column_for_a_guess(self):
    force = BruteForce()
    force.puzzle = [0, 1, 1, 1, 1, 1, 1, 1, 1, \
    2, 1, 1, 1, 1, 1, 1, 1, 1, \
    3, 1, 1, 1, 1, 1, 1, 1, 1, \
    4, 1, 1, 1, 1, 1, 1, 1, 1, \
    5, 1, 1, 1, 1, 1, 1, 1, 1, \
    6, 1, 1, 1, 1, 1, 1, 1, 1, \
    7, 1, 1, 1, 1, 1, 1, 1, 1, \
    8, 1, 1, 1, 1, 1, 1, 1, 1, \
    9, 1, 1, 1, 1, 1, 1, 1, 1]
    guess = 1
    index = 0
    self.assertTrue(force.valid_for_column(index, guess))

  def test_validation_of_block_for_a_guess(self):
    force = BruteForce()
    force.puzzle = [1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 2, 3, 1, 1, 1, \
    1, 1, 1, 4, 0, 6, 1, 1, 1, \
    1, 1, 1, 7, 8, 9, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1, \
    1, 1, 1, 1, 1, 1, 1, 1, 1]
    guess = 5
    index = 45
    self.assertTrue(force.valid_for_block(index, guess))

if __name__ == '__main__':
  unittest.main()