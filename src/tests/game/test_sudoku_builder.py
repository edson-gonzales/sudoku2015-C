"""
This module is in charge of testing the different types of Grid generation for the Sudoku2015-C game 
performed by the SudokuBuilder class.
"""
import unittest
from ...game.sudoku_builder import SudokuBuilder


class TestSudokuBuilder(unittest.TestCase):

    def test_sudoku_builder_can_be_created_successfully(self):
        visible_numbers = 20
        builder = SudokuBuilder(visible_numbers)
        self.assertIsInstance(builder, SudokuBuilder)

    def test_sudoku_builder_can_generate_random_grids_of_81_chars(self):
        visible_numbers = 20
        builder = SudokuBuilder(visible_numbers)
        generated_string = builder.build_random_grid()
        self.assertEquals(81, len(generated_string))

    def test_sudoku_builder_generates_N_or_more_visible_numvers(self):
        visible_numbers = 20
        builder = SudokuBuilder(visible_numbers)
        generated_string = builder.build_random_grid()
        self.assertGreaterEqual(81-visible_numbers, generated_string.count('0'))

    def test_shuffled_does_not_change_the_contents_just_the_sequence(self):
        expected_result = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        visible_numbers = 20
        builder = SudokuBuilder(visible_numbers)
        actual_result = builder.shuffled(expected_result)
        self.assertItemsEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
