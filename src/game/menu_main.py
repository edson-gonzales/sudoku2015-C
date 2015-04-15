""" MenuMain module presents the main options to the user when the program starts"""

from menu_settings import MenuSettings
from menu_solver import MenuSolver
from collections import OrderedDict
import time

class MenuMain(object):
	def __init__(self):
		""" Initializes the control menu variables and starts the loop"""
		self.options = None
		self.current_response = None
		self.continue_main_menu = True
		self.menu_settings = None
		self.menu_solver = None
		self.main_menu_completed = False
		self.main_loop()

	def show_main_menu(self):
		"""
		Prints the main menu header and calls the remaining menu options along with 
		validators and manager
		"""
		print("~~~~~~~~~~~~~~~~~~~~~~~~")
		print("SUDOKU 2015-C MAIN MENU")
		print("~~~~~~~~~~~~~~~~~~~~~~~~")
		print("Loading available Menu Options...")
		time.sleep(2)
		self.define_main_options()
		print(self.__show_multiple_options())
		if self.__validate_user_response():
			print("\nOption selected: '%s'. Executing the action..\n" %(self.options[self.current_response]))
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
		if self.current_response == "1":
			self.menu_settings = MenuSettings()
			self.menu_settings.show_current_configuration()
			self.main_menu_completed = True
		elif self.current_response == "2":
			self.menu_settings = MenuSettings()
			self.menu_settings.show_settings_menu()
			self.main_menu_completed = True
		elif self.current_response == "3":
			self.menu_settings = MenuSettings()
			self.menu_solver = MenuSolver(self.menu_settings.retrieve_default_settings())
			self.main_menu_completed = True
		elif self.current_response == "4":
			print("This feature will be soon implemented")
			self.main_menu_completed = True
		elif self.current_response == "5":
			self.main_menu_completed = False

	def __validate_user_response(self):
		""" Evaluates the user response in a loop until a correct answer is set.
		Keyword arguments:
		options -- dictionary of all the main menu options.
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

	def main_loop(self):
		""" Create a loop where the main menu can be displayed again if the user desires so.
		And also provides a friendly way to exit the program
		"""
		while self.continue_main_menu:
			self.show_main_menu()
			if self.main_menu_completed:
				if self.__eval_y_n('\nMain Menu executed successfully, Would you like to view it again? '):
					self.continue_main_menu = True
				else:
					print("\nClosing App...")
					time.sleep(2)
					break
			else:
				if self.__eval_y_n('\nWould you really want to close the Sudoku 2015-C application?'):
					print("\nClosing App...")
					time.sleep(2)				
					break
				else:
					self.continue_main_menu = True
