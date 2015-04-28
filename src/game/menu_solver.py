""" MenuSolver module presents the solve options to the user when the action is chosen in MenuMain module"""

from menu_base import MenuBase
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
        """
        super(MenuSolver, self).__init__()
        self.options = None
        self.current_response = None
        self.continue_solver_menu = True
        self.solver_menu_completed = False
        self.default_settings = default_settings
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
        time.sleep(2)
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
            print("This feature will be soon implemented")
        elif self.current_response == "2":
            print("This feature will be soon implemented")
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
        txt, csv, cmd, or random"""
        algorithm = self.default_settings['algorithm']
        level = self.default_settings['level']
        min_d = int(self.default_settings['min'])
        max_d = int(self.default_settings['max'])
        starting_digits = random.randint(min_d, max_d)
        print("1. Using the '%s' default algorithm to solve the Sudoku Puzzle " %(algorithm))
        if mode == 'random':
            print("2. Using the '%s' default level to solve the Sudoku Puzzle " %(level))
            print("3. Using '%s' starting digits to solve the Sudoku Puzzle\n " %(starting_digits))

        class_name = self.default_settings['algorithm'].translate(None, ' ')
        class_name += '()'
        getattr(self.sudoku_solver, 'change_algorithm')(eval(class_name))
        if mode == 'random':
            self.sudoku_solver.solve_sudoku_from_grid_generated(starting_digits)
        elif mode == 'cmd':
            self.sudoku_solver.solve_sudoku_from_string_provided(self.current_response)

        print (self.sudoku_solver.display_grid_source_with_format())
        print (self.sudoku_solver.display_grid_result_with_format())

    def manage_cmd_input_string(self):
        """Validates the user input and then generate the puzzle solution"""
        if super(MenuSolver, self).validate_puzzle_string():
            print("\nCommand line successfully read. Processing the request...\n")
            time.sleep(2)
            self.generate_puzzle_solution('cmd')

