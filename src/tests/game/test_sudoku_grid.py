"""
This module is in charge of testing the different types of Grid for the Sudoku2015-C game 
performed by the SudokuGrid class.
"""
import unittest
from ...game.sudoku_grid import SudokuGrid


class TestSudokuGrid(unittest.TestCase):

  def test_sudoku_grid_can_be_created_with_no_arguments(self):
    grid = SudokuGrid()
    self.assertIsInstance(grid, SudokuGrid)

  def test_rows_and_cols_indexes_can_be_crossed(self):
    grid = SudokuGrid()
    rows = 'ABC'
    cols = '123'
    expected_result = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    actual_result = grid.cross(rows, cols)
    self.assertEquals(expected_result, actual_result)

  def test_grid_values_can_be_loaded_in_a_dictionary(self):
    # Establishing the expected result
    values = "012340567"
    crossed_index = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    expected_result = {'A1': '0', 'A2': '1', 'A3': '2', 'B1': '3', 'B2': '4', 'B3': '0', \
    'C1': '5', 'C2': '6', 'C3': '7'}
    # Establishing the actualresult
    grid = SudokuGrid()
    grid.squares = crossed_index
    grid.load_grid_values(values)
    actual_result = grid.grid_values
    # Comparing dictionaries: only the item's values, item's order does not matter.
    self.assertItemsEqual(expected_result, actual_result)

  def test_simple_grid_formatting(self):
    expected_result = "\n123456789\n123456789\n123456789\n123456789\n12345"+\
     "6789\n123456789\n123456789\n123456789\n123456789\n"
    s_grid = "123456789123456789123456789123456789123456789123456789123456789123456789123456789"
    grid = SudokuGrid()
    grid.load_grid_values(s_grid)
    self.assertEquals(expected_result, grid.display_simple_grid())

  def test_2D_formatting(self):
    expected_result = ""
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "------+------+------" + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "------+------+------" + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"
    expected_result += "1 2 3 |4 5 6 |7 8 9 " + "\n"

    s_grid = "123456789123456789123456789123456789123456789123456789123456789123456789123456789"
    grid = SudokuGrid()
    grid.load_grid_values(s_grid)
    self.assertEquals(expected_result, grid.display_2D_grid())


if __name__ == '__main__':
  unittest.main()
