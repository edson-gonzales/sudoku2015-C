""" MenuMain module presents the main options to the user when the program starts"""

from menu_base import MenuBase
from menu_settings import MenuSettings
from menu_solver import MenuSolver
from sudoku_live_game import SudokuLiveGame
from collections import OrderedDict
import time

class MenuMain(MenuBase):
    def __init__(self):
        """ Initializes the control menu variables and starts the loop
        Note: This subclass is going to inherit useful and generic methods of MenuBase superclass
        """
        super(MenuMain, self).__init__()
        self.options = None
        self.current_response = None
        self.continue_main_menu = True
        self.menu_settings = None
        self.menu_solver = None
        self.sudoku_game = None
        self.main_menu_completed = False
        self.main_loop()

    def show_main_menu(self):
        """
        Prints the main menu header and calls the remaining menu options along with
        validators and manager
        """ 
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
        print("SUDOKU 2015-C MAIN MENU")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Loading available Menu Options...")
        time.sleep(1)
        self.define_main_options()
        print (super(MenuMain, self).build_multiple_options())
        if super(MenuMain, self).validate_user_response():
            print("\nOption selected: '%s'. Executing...\n" %(self.options[self.current_response]))
            time.sleep(2)
            self.manage_menu_options()

    def define_main_options(self):
        """
        Creates an Ordered Dictionary data structure to store the available options for the
        main menu.
        """
        self.options = (
        ("1", "View Default Game Settings" ),
        ("2", "Modify Sudoku Game and Puzzle Settings"),
        ("3", "Use Strategies/Algorithms to solve Sudoku Puzzles"),
        ("4", "Start a new Sudoku Live Game"),
        ("5", "Quit Main Program"))
        self.options = OrderedDict(self.options)

    def manage_menu_options(self):
        """
        Run certain actions according to the selected option chosed by the user.
        """
        self.menu_settings = MenuSettings()
        self.main_menu_completed = True
        if self.current_response == "1":        
            self.menu_settings.show_current_configuration()
        elif self.current_response == "2":
            self.menu_settings.show_settings_menu()
        elif self.current_response == "3":
            self.menu_solver = MenuSolver(self.menu_settings.retrieve_default_settings())
        elif self.current_response == "4":
            self.sudoku_game = SudokuLiveGame(self.menu_settings.retrieve_default_settings())
        elif self.current_response == "5":
            self.main_menu_completed = False

    def main_loop(self):
        """ Create a loop where the main menu can be displayed again if the user desires so.
        And also provides a friendly way to exit the program
        """
        while self.continue_main_menu:
            self.show_main_menu()
            self.continue_main_menu = self.handle_main_loop_according_response()
            if self.continue_main_menu is False:
                break

    def handle_main_loop_according_response(self):
        """ When a certain action menu is completed the user can run again the main menu module
        or leave the app, and a confirmation message is displayed in order to leave the module.
        """
        if self.main_menu_completed:
            question = '\nMain Menu executed successfully, Would you like to view it again? '
            if super(MenuMain, self).eval_y_n(question):
                return True
            else:
                print("\nClosing App...")
                time.sleep(2)
                return False
        else:
            question = '\nWould you really want to close the Sudoku 2015-C application?'
            if super(MenuMain, self).eval_y_n(question):
                print("\nClosing App...")
                time.sleep(2)
                return False
            else:
                return True
