""" MenuBase class presents the generic methods and attributes that will be used
by MenuMain and MenuSolver modules"""

class MenuBase(object):
    """ Initializes the options dictionary and the response variables"""
    def __init__(self):
        self.options = None
        self.current_response = None

    def ask_user_input(self, sentence):
        """ Reads the user input and returns its response.
        Keyword arguments:
        sentence -- the sentence that will be displayed in command line.
        """
        user_input = raw_input(sentence + " : ")
        return user_input

    def eval_y_n(self, question):
        """ Reads the user input appending 'y/n' characters at the end
        Keyword arguments:
            question -- the question that will be displayed in command line.
        Returned parameter:
            true or false -- evaluates the user response to true if it is ('y', 'yes') in any case
        """
        answer = raw_input(question + " [y/n] : ")
        return answer.lower() in ['y', 'yes']

    def build_multiple_options(self):
        """ Provides a sorted menu of all menu items available
        Keyword arguments:
            options -- Dictionary of all options with a certain menu item.
        Returned value:
            multiple_options -- a formatted string with all the options stored
        in self.options dictionary.(E.g. [1] Option A [2] Option B and so on..)
        """
        multiple_options = ""
        for index, option in self.options.iteritems():
            multiple_options += "\n[" + index + "] " + option
        multiple_options += "\n"
        return multiple_options

    def validate_user_response(self):
        """ Evaluates the user response in a loop until a correct answer is set.
        Keyword arguments:
            options -- dictionary of all the main menu options.
        Returned parameter:
            is_response_valid -- return True if the user chooseS one of the valid keys of the
                dictionary self.options
        """
        is_response_valid = False
        while is_response_valid is False:
            response = self.ask_user_input("Please, enter a valid option or command")
            if response in self.options.keys():
                is_response_valid = True
                self.current_response = response
            else:
                print("Invalid option/command, please try again")
        return is_response_valid

    def validate_correct_hint(self):
        """ Return True once the User entera a valid hint threshold,
        that should be a digt between 0 and 81
        """
        is_response_hint_valid = False
        while is_response_hint_valid is False:
            hint_value = self.ask_user_input("Enter maximum hint threshold")
            if not hint_value.isdigit():
                print("Not a number, please try again")
            elif 0 <= int(hint_value) <= 81:
                is_response_hint_valid = True
                self.current_response = hint_value
            else:
                print("Number is out of the valid range, please try again")
        return is_response_hint_valid

    def validate_puzzle_param(self, name):
        """ Return True once the User entera a valid hint threshold,
        that should be a digt between 0 and 81
        """
        is_puzzle_parameter_valid = False
        while is_puzzle_parameter_valid is False:
            puzzle_parameter = self.ask_user_input("Enter a valid '" + name + "'")
            if not puzzle_parameter.isdigit():
                print("Not a number, please try again")
            elif 1 <= int(puzzle_parameter) <= 9:
                is_puzzle_parameter_valid = True
                self.current_response = puzzle_parameter
            else:
                print("Number is out of the valid range (1 to 9), please try again")
        return is_puzzle_parameter_valid
