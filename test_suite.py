# from src.game.menu_settings import MenuSettings
import unittest
from src.settings import settings
from src.tests.handlers.test_xml_handler import TestXMLHandler
from src.tests.game.test_sudoku_builder import TestSudokuBuilder
from src.tests.game.test_sudoku_grid import TestSudokuGrid
from src.tests.game.test_sudoku_solver import TestSudokuSolver
from src.tests.algorithms.test_algorithm import TestAlgorithm
from src.tests.algorithms.test_brute_force import TestBruteForce

settings.init()

xml_suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLHandler)

sudoku_builder_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuBuilder)

sudoku_grid_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuGrid)

sudoku_solver_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuSolver)

algorithm_suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgorithm)

brute_force_suite = unittest.TestLoader().loadTestsFromTestCase(TestBruteForce)

alltests = unittest.TestSuite([xml_suite, sudoku_builder_suite, sudoku_grid_suite, sudoku_solver_suite, algorithm_suite, brute_force_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)
