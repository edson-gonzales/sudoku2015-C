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
        st_grd = '517600034289004000346205090602000010038006047000000000090000078703400560000000000'
        backtracking.load_puzzle(st_grd)
        expected = [\
        [5, 1, 7, 6, 0, 0, 0, 3, 4],\
        [2, 8, 9, 0, 0, 4, 0, 0, 0],\
        [3, 4, 6, 2, 0, 5, 0, 9, 0],\
        [6, 0, 2, 0, 0, 0, 0, 1, 0],\
        [0, 3, 8, 0, 0, 6, 0, 4, 7],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 9, 0, 0, 0, 0, 0, 7, 8],\
        [7, 0, 3, 4, 0, 0, 5, 6, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEquals(expected, backtracking.grid)

    def test_puzzle_is_solved_correctly(self):
        string = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
        backtracking = Backtracking()
        backtracking.solve_sudoku(string)
        expect = "483921657967345821251876493548132976729564138136798245372689514814253769695417382"
        actual_result = backtracking.retrieve_grid_basic_format()
        self.assertEquals(expect, actual_result)

    def test_puzzle_can_be_formated_as_valid_output(self):
        backtracking = Backtracking()
        backtracking.grid = [\
        [5, 1, 7, 6, 0, 0, 0, 3, 4],\
        [2, 8, 9, 0, 0, 4, 0, 0, 0],\
        [3, 4, 6, 2, 0, 5, 0, 9, 0],\
        [6, 0, 2, 0, 0, 0, 0, 1, 0],\
        [0, 3, 8, 0, 0, 6, 0, 4, 7],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0],\
        [0, 9, 0, 0, 0, 0, 0, 7, 8],\
        [7, 0, 3, 4, 0, 0, 5, 6, 0],\
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        expect = '517600034289004000346205090602000010038006047000000000090000078703400560000000000'
        actual_result = backtracking.retrieve_grid_basic_format()
        self.assertEquals(expect, actual_result)

    def test_puzzle_correcteness_validator(self):
        backtracking = Backtracking()
        backtracking.grid = [\
        [7, 5, 1, 8, 4, 3, 9, 2, 6],\
        [8, 1, 3, 23, 2, 5, 1, 7, 4],\
        [1, 4, 2, 1, 7, 9, 5, 8, 3],\
        [4, 2, 5, 3, 1, 6, 7, 9, 8],\
        [1, 7, 6, 9, 8, 2, 3, 4, 5],\
        [9, 1, 8, 7, 5, 4, 6, 1, 9],\
        [3, 6, 1, 2, 9, 7, 8, 9, 1],\
        [2, 8, 9, 5, 3, 1, 9, 6, 7],\
        [5, 1, 7, 4, 6, 8, 2, 3, 9]]
        self.assertFalse(backtracking.validate_puzzle())
        backtracking.grid = [\
        [7, 5, 1, 8, 4, 3, 9, 2, 6],\
        [8, 9, 3, 6, 2, 5, 1, 7, 4],\
        [6, 4, 2, 1, 7, 9, 5, 8, 3],\
        [4, 2, 5, 3, 1, 6, 7, 9, 8],\
        [1, 7, 6, 9, 8, 2, 3, 4, 5],\
        [9, 3, 8, 7, 5, 4, 6, 1, 2],\
        [3, 6, 4, 2, 9, 7, 8, 5, 1],\
        [2, 8, 9, 5, 3, 1, 4, 6, 7],\
        [5, 1, 7, 4, 6, 8, 2, 3, 9]]
        self.assertTrue(backtracking.validate_puzzle())


if __name__ == '__main__':
  unittest.main()
