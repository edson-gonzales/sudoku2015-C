# from src.game.menu_settings import MenuSettings
import unittest
from src.settings import settings
from src.tests.handlers.test_xml_handler import TestXMLHandler
from src.tests.handlers.test_txt_handler import TestTXTHandler
from src.tests.handlers.test_csv_handler import TestCSVHandler
from src.tests.game.test_sudoku_builder import TestSudokuBuilder
from src.tests.game.test_sudoku_grid import TestSudokuGrid
from src.tests.game.test_sudoku_solver import TestSudokuSolver
from src.tests.algorithms.test_algorithm import TestAlgorithm
from src.tests.algorithms.test_brute_force import TestBruteForce
from src.tests.algorithms.test_peter_norvig import TestPeterNorvig
from src.tests.algorithms.test_backtracking import TestBacktracking

settings.init()

xml_suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLHandler)

txt_suite = unittest.TestLoader().loadTestsFromTestCase(TestTXTHandler)

csv_suite = unittest.TestLoader().loadTestsFromTestCase(TestCSVHandler)

sudoku_builder_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuBuilder)

sudoku_grid_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuGrid)

sudoku_solver_suite = unittest.TestLoader().loadTestsFromTestCase(TestSudokuSolver)

algorithm_suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgorithm)

brute_force_suite = unittest.TestLoader().loadTestsFromTestCase(TestBruteForce)

peter_norvig_suite = unittest.TestLoader().loadTestsFromTestCase(TestPeterNorvig)

backtracking_suite = unittest.TestLoader().loadTestsFromTestCase(TestBacktracking)

alltests = unittest.TestSuite([xml_suite, txt_suite, csv_suite, sudoku_builder_suite, sudoku_grid_suite,\
 sudoku_solver_suite, algorithm_suite, brute_force_suite, peter_norvig_suite, backtracking_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)
