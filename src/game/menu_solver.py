""" MenuSolver module presents the solve options to the user when the action is chosen in MenuMain module"""

from menu_base import MenuBase
from menu_file_explorer import MenuFileExplorer
from ..game.sudoku_solver import SudokuSolver
from ..algorithms.algorithm import Algorithm
from ..algorithms.brute_force import BruteForce
from ..algorithms.backtracking import Backtracking
from ..algorithms.peter_norvig import PeterNorvig
from collections import OrderedDict
import time
import random
import sys


class MenuSolver(MenuBase):
    def __init__(self, default_settings):
        """ Initializes the control menu variables and starts the loop
        Note: This subclass is going to inherit useful and generic methods of MenuBase superclass
        Keyword arguments:
            default_settings : This is a dictionary provided by XMLHandler with the current
            default game settings
        """
        super(MenuSolver, self).__init__()
        self.options = None
        self.current_response = None
        self.continue_solver_menu = True
        self.solver_menu_completed = False
        self.file_explorer = None
        self.default_settings = default_settings
        self.algorithm = None
        self.level = None
        self.min_digit = None
        self.max_digit = None
        self.starting_digits = None
        self.sudoku_solver = SudokuSolver()
        self.solver_loop()

    def show_solver_menu(self):
        """
        Prints the solver menu header and calls the remaining menu options along with
        validators and manager
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("SUDOKU 2015-C SOLVER MODULE")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Loading available Menu Options...")
        time.sleep(1)
        self.define_solver_options()
        print(super(MenuSolver, self).build_multiple_options())
        if super(MenuSolver, self).validate_user_response():
            print("\nOption selected: '%s'. Executing...\n" %(self.options[self.current_response]))
            time.sleep(2)
            self.manage_menu_options()

    def define_solver_options(self):
        """
        Creates an Ordered Dictionary data structure to store the available options for the
        solver menu.
        """
        self.options = (
        ("1", "Read TXT file which contains an unresolved Sudoku Puzzle" ),
        ("2", "Read CSV file which contains an unresolved Sudoku Puzzle"),
        ("3", "Read an unresolved Sudoku Puzzle from command line"),
        ("4", "Generate a random unresolved Sudoku Puzzle"),
        ("5", "Quit Solver Module"))
        self.options = OrderedDict(self.options)

    def manage_menu_options(self):
        """
        Run certain actions according to the selected option chosed by the user.
        """
        self.solver_menu_completed = True
        if self.current_response == "1":
            self.file_explorer = MenuFileExplorer('txt')
            self.generate_puzzle_solution('txt')
        elif self.current_response == "2":
            self.file_explorer = MenuFileExplorer('csv')
            self.generate_puzzle_solution('csv')
        elif self.current_response == "3":
            self.manage_cmd_input_string()
        elif self.current_response == "4":
            self.generate_puzzle_solution('random')
        elif self.current_response == "5":
            self.solver_menu_completed = False


    def solver_loop(self):
        """ Create a loop where the solver menu can be displayed again if the user desires so.
        And also provides a friendly way to exit the menu level
        """
        while self.continue_solver_menu:
            self.show_solver_menu()
            self.continue_solver_menu = self.handle_solver_loop_according_response()
            if self.continue_solver_menu is False:
                break

    def handle_solver_loop_according_response(self):
        """ When a certain action menu is completed the user can run again the solver menu module
        or leave the module, and a confirmation message is displayed in order to leave the module.
        """
        if self.solver_menu_completed:
            question = '\nSolver Module executed successfully, Would you like to use it again?'
            if super(MenuSolver, self).eval_y_n(question):
                return True
            else:
                print("\nClosing Solver Module...")
                time.sleep(2)
                return False
        else:
            question = '\nWould you really want to close Solver Module and go back to Main Menu?'
            if super(MenuSolver, self).eval_y_n(question):
                print("\nClosing Solver Module...")
                time.sleep(2)
                return False
            else:
                return True

    def generate_puzzle_solution(self, mode='random'):
        """Retrieve the current XML configuration and generates a puzzle solution using the
        XML parameters and also use the mode method parameter to decide the source of the grid:
        txt, csv, cmd, or random
        Keyword arguments:
            mode -- parameter that will vary from random, txt and csv to display and use the
            correct resolution methods.
        """
        self.set_game_settings()
        print("1. Using '%s' default algorithm to solve Sudoku Puzzle" %(self.algorithm))
        class_name = self.default_settings['algorithm'].translate(None, ' ') + '()'
        getattr(self.sudoku_solver, 'change_algorithm')(eval(class_name))
        if mode == 'random':
            print("2. Using the '%s' default level to solve the Sudoku Puzzle " %(self.level))
            print("3. Using '%s' starting digits to create the Puzzle\n " %(self.starting_digits))
            self.sudoku_solver.solve_sudoku_from_grid_generated(self.starting_digits)
            self.display_sudoku_puzzle_results("2D_point")
        elif mode == 'cmd':
            self.sudoku_solver.solve_sudoku_from_string_provided(self.current_response)
            self.display_sudoku_puzzle_results("2D_point")
        elif mode == 'txt' or mode == 'csv':
            method_name = "solve_sudoku_from_" + mode + "_file"
            try:
                getattr(self.sudoku_solver, method_name)(self.file_explorer.file_chosen)
                self.display_sudoku_puzzle_results()
            except ValueError:
                pass 
        
    def display_sudoku_puzzle_results(self, format_type="simple"):
        """
        Displays the unresolved and resolved grids using simple, 2D or 2D_point formats
        Keyword arguments:
            format_type -- initially can take the simple, 2D and 2D_point format types.
        """
        print (self.sudoku_solver.display_grid_source_with_format(format_type))
        print (self.sudoku_solver.display_grid_result_with_format(format_type))

    def set_game_settings(self):
        """The contructor parameter default settings is accessed to extract the game settings"""
        self.algorithm = self.default_settings['algorithm']
        self.level = self.default_settings['level']
        self.min_digit = int(self.default_settings['min'])
        self.max_digit = int(self.default_settings['max'])
        self.starting_digits = random.randint(self.min_digit, self.max_digit)


    def manage_cmd_input_string(self):
        """Validates the user input and then generate the puzzle solution"""
        if super(MenuSolver, self).validate_puzzle_string():
            print("\nCommand line successfully read. Processing the request...\n")
            time.sleep(2)
            self.generate_puzzle_solution('cmd')
