""" MenuSolver module presents the solve options to the user when the action is chosen in MenuMain module"""

from ..handlers.file_handler import FileHandler
from ..handlers.txt_handler import TXTHandler
from ..handlers.csv_handler import CSVHandler
from ..game.sudoku_solver import SudokuSolver
from ..algorithms.algorithm import Algorithm
from ..algorithms.brute_force import BruteForce
from collections import OrderedDict
import time
import random
import sys

class MenuSolver():
	def __init__(self, default_settings):
		""" Initializes the control menu variables and starts the loop"""
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
		print(self.__show_multiple_options())
		if self.__validate_user_response():
			print("\nOption selected: '%s'. Executing the action..\n" %(self.options[self.current_response]))
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
		if self.current_response == "1":
			print("This feature will be soon implemented")
			self.solver_menu_completed = True
		elif self.current_response == "2":
			print("This feature will be soon implemented")
			self.solver_menu_completed = True
		elif self.current_response == "3":
			print("This feature will be soon implemented")
			self.solver_menu_completed = True
		elif self.current_response == "4":
			self.menu_action_generate_resolve_puzzle()
			self.solver_menu_completed = True
		elif self.current_response == "5":
			self.solver_menu_completed = False

	def __validate_user_response(self):
		""" Evaluates the user response in a loop until a correct answer is set.
		Keyword arguments:
		options -- dictionary of all the solver menu options.
		"""
		is_response_valid = False
		while is_response_valid is False:
		 response = self.__ask_user_input("Please, enter a valid option number")
		 if response in self.options.keys():
		 	is_response_valid = True
		 	self.current_response = response
		 else:
		 	print("Invalid option number, please try again")
		return is_response_valid

	def __ask_user_input(self, sentence):
		""" Calls the python 2 raw_input method appending a colon character.
		Keyword arguments:
		sentence -- the sentence that will be displayed in command line.
		"""
		user_input = raw_input(sentence + " : ")
		return user_input

	def __eval_y_n(self, question):
		""" Calls the python 2 raw_input method appending a colon character and y/n options,
		also evaluates the user response, if it is ('y', 'Y', 'Yes', 'YES', 'yes')
		Keyword arguments:
		question -- the question that will be displayed in command line.
		"""
		answer = raw_input(question + " [y/n] : ")
		return answer in ['y', 'Y', 'Yes', 'YES', 'yes']

	def __show_multiple_options(self):
		""" Provides a sorted menu of all menu items available
		Keyword arguments:
		options -- Dictionary of all options with a certain menu item.
		"""
		question = ""
		for index, option in self.options.iteritems():
			question += "\n[" + index + "] " + option
		question += "\n"
		return question

	def solver_loop(self):
		""" Create a loop where the solver menu can be displayed again if the user desires so.
		And also provides a friendly way to exit the menu level
		"""
		while self.continue_solver_menu:
			self.show_solver_menu()
			if self.solver_menu_completed:
				question = '\nSolver Module executed successfully, Would you like to use it again?'
				if self.__eval_y_n(question):
					self.continue_solver_menu = True
				else:
					print("\nClosing Solver Module...")
					time.sleep(2)
					break
			else:
				question = '\nWould you really want to close the Solver Module and go back to Main Menu?'
				if self.__eval_y_n(question):
					print("\nClosing Solver Module...")
					time.sleep(2)
					break
				else:
					self.continue_solver_menu = True

	def menu_action_generate_resolve_puzzle(self):
		algorithm = self.default_settings['algorithm']
		level = self.default_settings['level']
		min_d = int(self.default_settings['min'])
		max_d = int(self.default_settings['max'])
		starting_digits = random.randint(min_d, max_d)
		print("1. Using the '%s' default algorithm to solve the Sudoku Puzzle " %(algorithm))
		print("2. Using the '%s' default level to solve the Sudoku Puzzle " %(level))
		print("3. Using '%s' starting digits to solve the Sudoku Puzzle\n " %(starting_digits))

		class_name = self.default_settings['algorithm'].translate(None, ' ')
		class_name += '()'
		getattr(self.sudoku_solver, 'change_algorithm')(eval(class_name))

		self.sudoku_solver.solve_sudoku_from_grid_generated(starting_digits)
		print (self.sudoku_solver.display_grid_source_with_format())
		print (self.sudoku_solver.display_grid_result_with_format())


