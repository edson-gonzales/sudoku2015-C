""" This module will be in charge of solving a the grid managed by SudokuBuilder and display it
in any format desired
"""
from sudoku_builder import SudokuBuilder
from sudoku_grid import SudokuGrid
from ..algorithms.algorithm import Algorithm
from ..algorithms.brute_force import BruteForce
from ..handlers.txt_handler import TXTHandler
from ..handlers.csv_handler import CSVHandler

class SudokuSolver(object):

    def __init__(self, algorithm=BruteForce()):
        """
        Initializes important parameters like Algorithm and SudokuGrid modules.
        Keyword arguments:
            algorithm -- type of strategy used to solve the sudoku puzzle
        """
        self.builder = None
        self.algorithm = algorithm
        self.string_grid = None
        self.string_grid_resolved = None
        self.sudoku_grid = SudokuGrid()
        self.txt_file = None
        self.csv_file = None
        self.command_line_input = None


    def solve_sudoku_from_txt_file(self, relative_path):
        """
        Loads a the sudoku puzzle from a txt file and it is resolved using the algorithm stored.
        Keyword arguments:
            relative_patch -- the real relative path to the txt file
            string_grid -- long string of 81 character where zeros represent empty spots.
        """
        self.txt_file = TXTHandler()
        self.txt_file.load_file(relative_path)
        self.string_grid = self.txt_file.retrieve_txt_grid()
        if self.is_string_grid_valid():
            self.sudoku_grid.load_grid_values(self.string_grid)
            self.algorithm.solve_sudoku(self.string_grid)
            self.string_grid_resolved = self.algorithm.retrieve_grid_basic_format()

        else:
            print("Error 1001: The TXT grid should contain only numbers in each square")

    def solve_sudoku_from_csv_file(self, relative_path):
        """
        Loads a the sudoku puzzle from a csv file and it is resolved using the algorithm stored.
        Keyword arguments:
            relative_patch -- the real relative path to the txt file.
            string_grid -- long string of 81 character where zeros represent empty spots.
        """
        self.csv_file = CSVHandler()
        self.csv_file.load_file(relative_path)
        self.string_grid = self.csv_file.retrieve_csv_grid()
        if self.is_string_grid_valid():
            self.sudoku_grid.load_grid_values(self.string_grid)
            self.algorithm.solve_sudoku(self.string_grid)
            self.string_grid_resolved = self.algorithm.retrieve_grid_basic_format()
        else:
            print("Error 1002: The CSV grid should contain only numbers in each square")

    def solve_sudoku_from_grid_generated(self, visible_numbers):
        """ Generates a random puzzle and then proceed to solved it using the algortihm stored.
        Keyword arguments:
            visible_numbers -- quantity of numbers that will be filled in the puzzle, the rest
        of them will be zeros or empty spaces in UI/Command Line Interface
        """

        self.builder = SudokuBuilder(visible_numbers)
        self.string_grid = self.builder.build_random_grid()
        self.sudoku_grid.load_grid_values(self.string_grid)
        self.algorithm.solve_sudoku(self.string_grid)
        self.string_grid_resolved = self.algorithm.retrieve_grid_basic_format()

    def display_grid_source_with_format(self, format_type="simple"):
        """
        Displays the unresolved grid using simple or 2D formats
        Keyword arguments:
            format_type -- initially can take the simple and 2D format types.
        """
        if format_type == "simple":
            return self.sudoku_grid.display_simple_grid()
        elif format_type == "2D":
            return self.sudoku_grid.display_2D_grid()
        elif format_type == "2D_point":
            return self.sudoku_grid.display_2D_grid_with_points()
        else:
            return "Invalid Grid Puzzle format type requested"

    def display_grid_result_with_format(self, format_type="simple"):
        """
        Displays the resolved grid using simple or 2D formats
        Keyword arguments:
            format_type -- initially can take the simple and 2D format types.
        """
        self.sudoku_grid.load_grid_values(self.string_grid_resolved)

        if format_type == "simple":
            return self.sudoku_grid.display_simple_grid()
        elif format_type == "2D":
            return self.sudoku_grid.display_2D_grid()
        else:
            return "Invalid Grid Puzzle format type requested"

    def change_algorithm(self, new_algorithm):
        """ change the algorithm stated in the constructor method init """
        self.algorithm = new_algorithm

    def is_string_grid_valid(self):
        """ Checks if the long string with 81 characters contain only numbers in its content"""
        return self.string_grid.isdigit()
