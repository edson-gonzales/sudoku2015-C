""" This class will be in charge of generating a random Sudoku Puzzle using a Dictionary
provided by the SudokuGrid Module.
"""
import random
from sudoku_grid import SudokuGrid

class SudokuBuilder(object):

    def __init__(self, visible_numbers):
        """ Initializes a Grid without digits generated yet
        Keyword arguments:
        grid -- module that is able to build a dictionary of positions and values.
        visible_numbers -- quantity of numbers that will be filled in the puzzle, the rest
        of them will be zeros or empty spaces in UI/Command Line Interface
        """
        self.grid = SudokuGrid()
        self.visible_numbers = visible_numbers

    def build_random_grid(self):
        """Build a random puzzle with N or more assignments. Restart on contradictions.
        Note the resulting puzzle is not guaranteed to be solvable, but empirically
        about 99.8% of them are solvable. Some have multiple solutions.
        Returned arguments:
            A long string with 81 characters where zeros that represent empty cells
        """
        max_index = 8
        values = dict((square_pos, self.grid.digits) for square_pos in self.grid.squares)
        for square_pos in self.shuffled(self.grid.squares):
            if not self.assign(values, square_pos, random.choice(values[square_pos])):
                break
            digit_list = [values[square_pos] for square_pos in self.grid.squares if len(values[square_pos]) == 1]
            if len(digit_list) >= self.visible_numbers and len(set(digit_list)) >= max_index:
                return ''.join(values[square_pos] if len(values[square_pos]) == 1 else '0' for square_pos in self.grid.squares)
        return self.build_random_grid()

    def return_join_characters(self, value, square_pos):

        random_grid = ""
        for square_pos in self.grid.squares:
            if len(value) == 1:
                random_grid += ''.join(value)
            else:
                random_grid += '0'
        return random_grid

    def shuffled(self, seq):
        """Return a randomly shuffled copy of the input sequence.
        Keyword arguments:
            seq -- An array of squares. (E.g. [A1, A2, ...])
        Returned parameter:
            A shuffled sequence, its items should be randomly permuted of its original indexes.
        """
        seq = list(seq)
        random.shuffle(seq)
        return seq

    def assign(self, values, square_pos, digit):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected.
        Keyword arguments:
            values -- dict of possible values, {square: digits} (e.g. {'A1':'12349', 'A2':'8', ..})
            square_pos -- coordinate of a square position of type string (e.g. 'A2')
            digit -- it is content of a square of type string (e.g. '8')
        """
        other_values = values[square_pos].replace(digit, '')
        if all(self.eliminate(values, square_pos, second_digit) for second_digit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square_pos, digit):
        """Eliminate digit from values[square_pos]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected.
        Keyword arguments:
            values --  dict of possible values, {square: digits} (e.g. {'A1':'12349', 'A2':'8', ..})
            square_pos -- coordinate of a square position of type string (e.g. 'A2')
            digit -- it is content of a square of type string (e.g. '8')
        """
        if digit not in values[square_pos]:
            return values ## Already eliminated
        values[square_pos] = values[square_pos].replace(digit, '')
        ## (1) If a square s is reduced to one value, then eliminate second_digit from the peers.
        if len(values[square_pos]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[square_pos]) == 1:
            second_digit = values[square_pos]
            square_values = (self.eliminate(values, second_square, second_digit)\
            for second_square in self.grid.peers[square_pos])
            if not all(square_values):
                return False
        ## (2) If a unit unit is reduced to only one place for a value digit, then put it there.
        for unit in self.grid.units[square_pos]:
            digit_places = [square_pos for square_pos in unit if digit in values[square_pos]]
            if len(digit_places) == 0:
                return False ## Contradiction: no place for this value
            elif len(digit_places) == 1 and not self.assign(values, digit_places[0], digit):
                return False
        return values
