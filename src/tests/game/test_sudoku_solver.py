"""
This module is in charge of testing the different resolution methods for a SudokuGrid
performed by the SudokuSolver class.
"""
import unittest
from ...game.sudoku_solver import SudokuSolver
from ...algorithms.algorithm import Algorithm
from ...algorithms.brute_force import BruteForce
from ...algorithms.peter_norvig import PeterNorvig
from ...handlers.txt_handler import TXTHandler


class TestSudokuSolver(unittest.TestCase):

  def test_sudoku_solver_can_be_created_with_no_arguments(self):
    solver = SudokuSolver()
    self.assertIsInstance(solver, SudokuSolver)

  def test_sudoku_solver_can_be_created_with_arguments(self):
    solver = SudokuSolver(BruteForce())
    self.assertIsInstance(solver, SudokuSolver)

  def test_solver_for_grid_generated(self):
    solver = SudokuSolver(PeterNorvig())
    solver.solve_sudoku_from_grid_generated(20)
    print (solver.display_grid_source_with_format("2D"))
    print (solver.display_grid_result_with_format("2D"))
    self.assertEquals(0, solver.string_grid_resolved.count('0'))


  def test_solver_for_TXT_files_is_working_fine(self):
    solver = SudokuSolver(PeterNorvig())
    solver.solve_sudoku_from_txt_file("content/sources/file_t_001.txt")
    print (solver.display_grid_source_with_format())
    print (solver.display_grid_result_with_format())
    self.assertEquals(0, solver.string_grid_resolved.count('0'))

  def test_solver_for_CSV_files_is_working_fine(self):
    solver = SudokuSolver(BruteForce())
    solver.solve_sudoku_from_csv_file("content/sources/file_c_001.csv")
    print (solver.display_grid_source_with_format("2D"))
    print (solver.display_grid_result_with_format("2D"))
    self.assertEquals(0, solver.string_grid_resolved.count('0'))

  def test_change_algorithms(self):
    brute_force = BruteForce()
    solver = SudokuSolver(brute_force)
    self.assertIsInstance(solver.algorithm, BruteForce)
    peter_norvig = PeterNorvig()
    solver.change_algorithm(peter_norvig)
    self.assertIsInstance(solver.algorithm, PeterNorvig)
    # missing backtracking assert

  def test_string_valid(self):
    solver = SudokuSolver(PeterNorvig())
    solver.string_grid = "abc123"
    self.assertFalse(bool(solver.is_string_grid_valid()))


if __name__ == '__main__':
  unittest.main()
