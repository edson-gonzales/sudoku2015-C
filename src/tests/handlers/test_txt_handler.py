"""
This module is in charge of testing the basic I/O functionality required to load 
and save properly the TXT files for the Sudoku2015-C game
"""

import unittest

from ...handlers.txt_handler import TXTHandler

class TestTXTHandler(unittest.TestCase):

  def test_txt_handler_can_be_created_with_no_arguments(self):
    txt = TXTHandler()
    self.assertIsInstance(txt, TXTHandler)

  def test_file_checker_fails_when_path_is_wrong(self):
    txt = TXTHandler()
    invalid_path = "<invalid>path*/file$001.x"
    try:
      txt.load_file(invalid_path)
      self.fail("This invalid path cannot be accepted")
    except IOError:
      pass
  def test_handler_returns_a_long_string_without_spaces(self):
    txt = TXTHandler()
    txt.load_file("content/sources/file_t_001.txt")
    expected = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    actual_result = txt.retrieve_txt_grid()
    self.assertEquals(expected, actual_result)


if __name__ == '__main__':
    unittest.main()