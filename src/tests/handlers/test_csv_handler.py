"""
This module is in charge of testing the basic I/O functionality required to load 
and save properly the CSV files for the Sudoku2015-C game
"""

import unittest

from ...handlers.csv_handler import CSVHandler

class TestCSVHandler(unittest.TestCase):

    def test_csv_handler_can_be_created_with_no_arguments(self):
        csv = CSVHandler()
        self.assertIsInstance(csv, CSVHandler)

    def test_file_checker_fails_when_path_is_wrong(self):
        csv = CSVHandler()
        invalid_path = "<invalid>path*/file$001.x"
        try:
            csv.load_file(invalid_path)
            self.fail("This invalid path cannot be accepted")
        except IOError:
            pass
    def test_handler_returns_a_long_string_without_spaces(self):
        csv = CSVHandler()
        csv.load_file("content/sources/file_c_001.csv")
        expect = '200080300060070084030500209000105408000000000402706000301007040720040060004010003'
        actual_result = csv.retrieve_csv_grid()
        self.assertEquals(expect, actual_result)


if __name__ == '__main__':
        unittest.main()
