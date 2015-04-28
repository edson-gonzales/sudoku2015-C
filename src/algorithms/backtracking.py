"""
This module is going to use the backtracking algorithm to resolve 
the sudoku grid which will be specified here as a sequence of 81 characters.
"""
from algorithm import Algorithm
from algorithm import elapsed_time
from itertools import chain                                                             

class Backtracking(Algorithm):
    def __init__(self):
        """
        Initializes the variables that will be used througout the class.
        Keyword arguments:
            self.grid -- the input value that is a string of 81 characters where zeros represent
            empty values.
        """
        self.grid = None

    @elapsed_time
    def solve_sudoku(self, grid_basic_format):
        """
        Load the puzzle and solve it.
        Keyword arguments:
            grid_basic_format -- a  string with 81 digit characters where zeros represent empty values.
        """
        self.load_puzzle(grid_basic_format)
        self.solve_backtracking()

    def load_puzzle(self, grid_basic_format):
        """
        Receives a string with 81 characters and transforms it to a list of list
        Keyword arguments:
            grid_basic_format -- a  string with 81 digit characters where zeros represent empty spaces.
        Returned parameters:
             list_of_list  -- A  2-dimensional array of size 9 x 9 composed of integer values.
        """
        dimension = 9
        list_of_numbers = [int(n) for n in grid_basic_format]
        list_of_list = [[0] * dimension] * dimension
        for row in range(dimension):
            list_of_list[row] = list_of_numbers[row * dimension : (row + 1) * dimension]
        self.grid = list_of_list

    def find_next_cell_to_fill(self, start_x, start_y):
        """
        Return the cell that is unfilled, the cell that contains zero 0 value
        Keyword arguments:
            start_x -- row position where the search operation will start (e.g. from 3 to 9).
            start_y -- column position where the search operation will start (e.g. from 4 to 9).
        Returned parameters:
            cell_position -- tuple of values (pos_x, pos_y) where the first zero cell is found.
        """

        cell_position = None
        for pos_x in range(start_x, 9):
            cell_position = self.find_cell_in_row(pos_x, start_y)
            if cell_position is not None:
                return cell_position

        for pos_x in range(0, 9):
            cell_position = self.find_cell_in_row(pos_x, 0)
            if cell_position is not None:
                return cell_position

        if cell_position is None:
            cell_position = (-1, -1)

        return cell_position


    def find_cell_in_row(self, pos_x, start_y):
        """
        Look for the first cell that is unfilled in a specific row, cell should contain zero value
        Keyword arguments:
            pos_x -- specific row where the search will be performed.
            start_y -- column position where the search operation will start (e.g. from 4 to 9).
        Returned parameters:
            cell_position -- tuple of values (pos_x, pos_y) where the first zero cell is found.
        """
        cell_position = None
        for pos_y in range(start_y, 9):
            if self.grid[pos_x][pos_y] == 0:
                cell_position = (pos_x, pos_y)
                break
        return cell_position

    def is_valid_guess(self, pos_x, pos_y, guess):
        """
        Checks if the guess is not breaking the rule that establishes that a row, column and section
        should only have one occurrence of numbers from 1 to 9.
        Keyword arguments:
            pos_x -- specific row where the guess is located within the 2-dimensional array.
            pos_y -- specific column where the guess is located within the 2-dimensional array.
            guess -- value from 1 to 9 that will be checked if it is valid to solve the puzzle.
        """
        valid_guess = False
        if self.validate_row(pos_x, guess):
            if self.validate_column(pos_y, guess):
                valid_guess = self.validate_section(pos_x, pos_y, guess)
        return valid_guess

    def validate_row(self, pos_x, guess):
        """ Validates that the "guess" filled in an "pos_x" row is not breaking the puzzle rule
        that establishes that a row should only have one occurrence of numbers from 1 to 9.
        Keyword arguments:
            pos_x -- index that is tracking the row where the guess is located.
            guess -- value from 1 to 9 that will be validated in this method.
        """
        row_ok = all([guess != self.grid[pos_x][y_index] for y_index in range(9)])
        return row_ok

    def validate_column(self, pos_y, guess):
        """ Validates that the "guess" filled in an "pos_y" column is not breaking the puzzle rule
        that establishes that a column should only have one occurrence of numbers from 1 to 9.
        Keyword arguments:
            pos_y -- index that is tracking the column where the guess is located.
            guess -- value from 1 to 9 that will be validated in this method.
        """
        column_ok = all([guess != self.grid[x_index][pos_y] for x_index in range(9)])
        return column_ok

    def validate_section(self, pos_x, pos_y, guess):
        """ Validates that the "guess" filled in an coordinates (pos_x, pos_y) is not breaking the puzzle rule
        that establishes that a section should only have one occurrence of numbers from 1 to 9.
        Keyword arguments:
            pos_x -- index that is tracking the row where the guess is located.
            pos_y -- index that is tracking the column where the guess is located.
            guess -- value from 1 to 9 that will be validated in this method.
        Method parameters:
            sec_topx -- top row index of the puzzle section (block) where the guess belongs
            sec_topy -- top column index of the puzzle section (block) where the guess belongs
        """
        valid_section = True
        sec_topx, sec_topy = 3 *(pos_x/3), 3 *(pos_y/3)
        for x_index in range(sec_topx, sec_topx+3):
            valid_section = self.validate_section_row(x_index, sec_topy, guess)
            if valid_section is False:
                return valid_section
        return valid_section


    def validate_section_row(self, x_index, sec_topy, guess):
        """ Validates within the section row of the guess is valid given the respective section columns
        Keyword arguments:
            x_index -- index that is tracking the row where the guess is located.
            sec_topy -- top column index of the puzzle section (block) where the guess belongs
            guess -- value from 1 to 9 that will be validated in this method.
        """
        valid_section = True
        for y_index in range(sec_topy, sec_topy+3):
            if self.grid[x_index][y_index] == guess:
                valid_section = False
                break
        return valid_section

    def solve_backtracking(self, pos_x=0, pos_y=0):
        """
        Recursive Method which visits empty cells and start guessing filling numbers and calling
        the is_valid_guess() method which in turn will be in charge of verifying the correcteness
        of the guess, if the guess is valid it will be added to the puzzle,
        otherwise the method will be called recursively until every empty cell is filled
        Keyword arguments:
            pos_x -- specific row where the guess is located within the 2-dimensional array.
            pos_y -- specific column where the guess is located within the 2-dimensional array.
        """
        pos_x, pos_y = self.find_next_cell_to_fill(pos_x, pos_y)
        if pos_x == -1:
            return True
        for guess in range(1, 10):
            if not self.is_valid_guess(pos_x, pos_y, guess):
                continue
            self.grid[pos_x][pos_y] = guess
            if self.solve_backtracking(pos_x, pos_y): 
                return True
            self.grid[pos_x][pos_y] = 0
        return False

    def retrieve_grid_basic_format(self):
        """
        Overrides the retrieve_grid_basic_format superclass method, for this algorithm is required
            to convert the solution stored in a list of lists of 81 integers to a string of 81 characters
        Returned parameters:
            outcome -- a string of 81 characters converted from the 2-D array of 81 integers
        """
        outcome = ""
        for first_list in self.grid:
            for number in first_list:
                outcome += ''.join(str(number))
        return outcome

    def validate_puzzle(self):
        """
        Validates if the entire puzzle resolution is correct, by reviewing the rows, cols and blocks.
        True if all conditions are met, false otherwise.
        """
        def get_block(pos_x, pos_y):
            return chain(*[self.grid[i][3*pos_x:3*pos_x+3] for i in range(3*pos_y, 3*pos_y+3)])
        rows = [set(row) for row in self.grid]
        columns = [set(column) for column in zip(*self.grid)]
        blocks = []
        for pos_x in range(0, 3):
            for pos_y in range(0, 3):
                blocks.append(set(get_block(pos_x, pos_y)))
        return all(map(lambda s: len(s) == 9 and sum(s) == 45, rows + columns + blocks))
