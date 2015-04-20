"""
This module is in charge of testing the backtrracking algorithm base class
"""

import unittest
from ...algorithms.backtracking import Backtracking

class TestBacktracking(unittest.TestCase):

	def test_backtracking_can_be_created_with_no_arguments(self):
		backtracking = Backtracking()
		self.assertIsInstance(backtracking, Backtracking)

	def test_puzzle_can_be_formated_as_valid_input(self):
		backtracking = Backtracking()
		backtracking.load_puzzle('517600034289004000346205090602000010038006047000000000090000078703400560000000000')
		expected = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
		self.assertEquals(expected, backtracking.grid)

	def test_puzzle_is_solved_correctly(self):
		string = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
		backtracking = Backtracking()
		backtracking.solve_sudoku(string)
		expected_result = "483921657967345821251876493548132976729564138136798245372689514814253769695417382"
		actual_result = backtracking.retrieve_grid_basic_format()
		self.assertEquals(expected_result, actual_result)

	def test_puzzle_can_be_formated_as_valid_output(self):
		backtracking = Backtracking()
		backtracking.grid = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
		expected_result = ('517600034289004000346205090602000010038006047000000000090000078703400560000000000')
		actual_result = backtracking.retrieve_grid_basic_format()
		self.assertEquals(expected_result, actual_result)


if __name__ == '__main__':
  unittest.main()	