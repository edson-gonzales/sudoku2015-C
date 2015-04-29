""" SudokuLiveGame module in charge of accepting user commands to fill the sudoku proposed game"""
from menu_base import MenuBase
from ..game.sudoku_solver import SudokuSolver
from ..game.sudoku_grid import SudokuGrid
from ..algorithms.algorithm import Algorithm
from ..algorithms.brute_force import BruteForce
from ..algorithms.backtracking import Backtracking
from ..algorithms.peter_norvig import PeterNorvig
from collections import OrderedDict
import random
import time

class SudokuLiveGame(MenuBase):
    def __init__(self, default_settings):
        """ Initializes the control menu variables and starts the loop
        Note: This subclass is going to inherit useful and generic methods of MenuBase superclass
        Keyword arguments:
            default_settings : This is a dictionary provided by XMLHandler with the current
            default game settings
        """
        super(SudokuLiveGame, self).__init__()
        self.options, self.current_response = None, None
        self.continue_game = True
        self.max_hints, self.starting_digits = None, None
        self.default_settings = default_settings
        self.string_grid_formulated, self.string_grid, self.string_grid_resolved = "", "", ""
        self.pos_x, self.pos_y, self.puzzle_value, self.hints_provided = 0, 0, 0, 0
        self.number_of_rows, self.number_of_columns = 9, 9
        self.last_hint = None
        self.sudoku_grid = SudokuGrid()
        self.sudoku_solver = SudokuSolver()
        self.show_game_settings()
        self.initialize_formulated_puzzle()
        self.activate_game_loop()

    def show_game_settings(self):
        """ Shows the XML config settings that will be used througout the game. """
        level = self.default_settings['level']
        min_digit = int(self.default_settings['min'])
        max_digit = int(self.default_settings['max'])
        self.max_hints = int(self.default_settings['hints'])
        self.starting_digits = random.randint(min_digit, max_digit)
        print("1. Using the '%s' game difficulty level" %(level))
        print("2. Using '%s' starting digits (or more) to build the Sudoku Puzzle" %(self.starting_digits))
        print("3. The maximum number of hints for this level is '%s'\n " %(self.max_hints))

    def initialize_formulated_puzzle(self):
        """ Puzzle is generated and it is stored as a long string of 81 chars, 
        also the expected solution is stored in other long string"""
        class_name = self.default_settings['algorithm'].translate(None, ' ')
        class_name += '()'
        getattr(self.sudoku_solver, 'change_algorithm')(eval(class_name))
        self.sudoku_solver.solve_sudoku_from_grid_generated(self.starting_digits)
        print (self.sudoku_solver.display_grid_source_with_format("2D_point"))
        self.string_grid_formulated = self.sudoku_solver.string_grid
        self.string_grid = self.sudoku_solver.string_grid
        self.string_grid_resolved = self.sudoku_solver.string_grid_resolved

    def activate_game_loop(self):
        """Loop starts and will only be broken by typing 'quit' or finishing properly the game"""
        self.define_game_options()
        print(super(SudokuLiveGame, self).build_multiple_options())
        while self.continue_game:
            print("(type 'help' to see the command list)")
            if super(SudokuLiveGame, self).validate_user_response():
                self.run_game_command()


    def define_game_options(self):
        """
        Creates an Ordered Dictionary structure to store the available options for the game menu.
        """
        self.options = (
        ("help", "Show the list of available commands" ),
        ("fill", "Fill a value in a row x and column y of the puzzle"),
        ("clear", "Clear a value in a row x and column y of the puzzle"),
        ("hint", "Provide a hint in a row x and column y of the puzzle"),
        ("quit", "Quit the Game"))
        self.options = OrderedDict(self.options)

    def run_game_command(self):
        """
        Run certain actions according to the selected option chosed by the user.
        e.g. self.help() or self.fill()
        """
        getattr(self, self.current_response)()

    def help(self):
        """ Shows again the list of available commands."""
        print(super(SudokuLiveGame, self).build_multiple_options())
        self.continue_game = True

    def fill(self):
        """ User has to enter row, column and puzzle values to correctly fill and display 
        the current puzzle game progress"""
        if self.validate_parameters("fill"):
            self.fill_value_at_position()
            time.sleep(2)
            self.display_puzzle()
            self.continue_game = self.check_game_continuity()

    def clear(self):
        """ User has to enter row, column values to clear the corresponding cell and display
        a point instead the existing number"""
        if self.validate_parameters("clear"):
            self.clear_value_at_position()
            time.sleep(2)
            self.display_puzzle()
            self.continue_game = True

    def hint(self):
        """ User has to enter row, column to receive a hint that will be automatically filled
        and be displayed in the current puzzle game progress"""
        if self.hints_provided < self.max_hints:
            if self.validate_parameters("hint"):
                self.provide_hint_at_position()
                time.sleep(1)
                self.display_puzzle()           
                print("Hint '%s' automatically filled in (row: %s, column: %s)" \
                    %(self.last_hint, self.pos_x, self.pos_y))
                print("%s of %s Hints already used.) " %(self.hints_provided, self.max_hints))
                time.sleep(1)
                self.continue_game = self.check_game_continuity()
        else:
            print("Sorry, you have reached the maximum number of hints")
            self.continue_game = True

    def quit(self, type="completed"):
        """ User can leave the game loop anytime after confirming with a friendly message, and
        also the loop is skipped when the game was successfully filled with 81 correct numbers.
        False is returned in previous cases, otherwise True is returned and the gae continues
        """
        if type is None:
            question = '\nWould you really want to leave the game?, your progress will be discarded'
            if super(SudokuLiveGame, self).eval_y_n(question):
                print("\nClosing Live Game...")
                time.sleep(2)
                self.continue_game = False
                return self.continue_game
            else:
                self.continue_game = True
                return self.continue_game
        else:
            print("\nClosing Live Game...")
            time.sleep(2)
            self.continue_game = False
            return self.continue_game

    def validate_parameters(self, mode="fill"):
        """ User input is validated for each available mode type.
        e.g. for fill command, we validate 3 params from 1,2,...9 range 
        for hint and clear, we validate 2 params from 1,2,..9 range
        True is returned if all params are correct, False otherwise.
        """
        all_params_correct = False
        if mode == "fill":
            if super(SudokuLiveGame, self).validate_puzzle_param("row x"):
                self.pos_x = self.current_response
            if super(SudokuLiveGame, self).validate_puzzle_param("column y"):
                self.pos_y = self.current_response
            if super(SudokuLiveGame, self).validate_puzzle_param("puzzle value"):
                self.puzzle_value = self.current_response
                all_params_correct = True
        elif mode == "clear" or mode == "hint":
            if super(SudokuLiveGame, self).validate_puzzle_param("row x"):
                self.pos_x = self.current_response
            if super(SudokuLiveGame, self).validate_puzzle_param("column y"):
                self.pos_y = self.current_response
                all_params_correct = True
        return all_params_correct

    def fill_value_at_position(self):
        """Converts temporarily the long string to a list of chars to fill the value
        in a certain position, and then change it back to a long string."""
        position = self.get_position()
        grid_list = list(self.string_grid)
        grid_list[position] = self.puzzle_value
        self.string_grid = ''.join(grid_list)

    def clear_value_at_position(self):
        """Converts temporarily the long string to a list of chars to fill zero
        in a certain position, and then change it back to a long string."""
        position = self.get_position()
        grid_list = list(self.string_grid)
        grid_list[position] = '0'
        self.string_grid = ''.join(grid_list)

    def provide_hint_at_position(self):
        """Converts temporarily the long string to a list of chars to fill the hint
        in a certain position, and then change it back to a long string."""
        position = self.get_position()
        hint = self.get_hint(position)
        grid_list = list(self.string_grid)
        grid_list[position] = hint
        self.hints_provided += 1
        self.string_grid = ''.join(grid_list)

    def get_position(self):
        """Returns an 1-D position based on row, column potitions of 2-D structure."""
        row = int(self.pos_x) - 1
        column = int(self.pos_y)
        position = (row * self.number_of_columns) + column - 1
        return position

    def get_hint(self, position):
        """Looks for the hint based on the position in the prevously stored solution"""
        grid_list_resolved = list(self.string_grid_resolved)
        self.last_hint = grid_list_resolved[position]
        return self.last_hint

    def display_puzzle(self):
        """Loads user game's data in Sudoku Grid module and then displays it formatted in console"""
        self.sudoku_grid.load_grid_values(self.string_grid)
        print ("")
        print self.sudoku_grid.display_2D_grid_with_points()

    def check_game_continuity(self):
        """When all the data of the puzzle is different than zero or point, we start to check the
        game correctness .
        True is returned to continue the loop because the puzzle is not resolved yet
        False is returned to finish the loop becuase he puzzle has been properly solved."""
        if self.string_grid.count('0') == 0:
            return self.validate_game_correctness()
        else:
            return True

    def validate_game_correctness(self):
        """Reusing backtracking checker methods to verify that the solution provided by the user
        meets the sudoku resolution rules in row, columns and blocks,
        Leave the game if it is correctly solved, otherwise a warning message is displayed and
        the game continues"""
        validator = Backtracking()
        validator.load_puzzle(self.string_grid)
        if validator.validate_puzzle():
            print("Congratulations!!, the puzzle has being correctly solved")
            time.sleep(2)
            self.quit("completed")
            return False
        else:
            print("The puzzle is not correctly solved, clear mistakes or use hints")
            return True
