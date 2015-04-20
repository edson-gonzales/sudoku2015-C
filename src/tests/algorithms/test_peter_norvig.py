"""
This module is in charge of testing the different types of Grid generation for the Sudoku2015-C game 
performed by the SudokuBuilder class.
"""
import unittest
from ...algorithms.peter_norvig import PeterNorvig
from ...game.sudoku_grid import SudokuGrid

class TestPeterNorvig(unittest.TestCase):

  def test_peter_norvig_can_be_created(self):
    peter_norvig_algorithm = PeterNorvig()
    self.assertIsInstance(peter_norvig_algorithm, PeterNorvig)

  def test_puzzle_can_be_loaded(self):
    values = "012340567"
    crossed_index = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    expected_result = {'A1': '0', 'A2': '1', 'A3': '2', 'B1': '3', 'B2': '4', 'B3': '0', \
    'C1': '5', 'C2': '6', 'C3': '7'}
    
    grid = SudokuGrid()
    grid.squares = crossed_index
    grid.load_grid_values(values)

    peter_norvig_algorithm = PeterNorvig()
    peter_norvig_algorithm.sudoku_grid = grid
    actual_result =  peter_norvig_algorithm.sudoku_grid.grid_values
    self.assertItemsEqual(expected_result, actual_result)

  def test_can_convert_a_grid_to_a_dict_of_possible_values_with_zero_or_point_for_empty_values(self):
    peter_norvig_algorithm = PeterNorvig()
    grid_string = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    expected_result={'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
    self.assertEquals(expected_result, peter_norvig_algorithm.grid_values(grid_string))

  def test_peter_norvig_can_convert_a_grid_to_a_dict_of_possible_values(self):
    peter_norvig_algorithm = PeterNorvig()
    grid_string = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    expected_result={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
    self.assertEquals(expected_result, peter_norvig_algorithm.parse_grid(grid_string))

  

