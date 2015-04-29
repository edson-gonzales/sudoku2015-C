"""
This module is in charge of managing the basic I/O functionality required to setting up 
properly the CSV files for the Sudoku2015-C game
"""
import abc
import os
from file_handler import FileHandler
from ..settings import settings

class CSVHandler(FileHandler):
    """
    This derived class is based on the "FileHandler" base class which had abstract methods:
    load_file and save_file that will be fully implemented here.
    """

    def __init__(self):
        """ Defines the object attributes that will be used throughout this class."""
        self.csv_absolute_file_path = None
        self.csv_opened = None
        self.csv_file = None

    def load_file(self, input_source):
        """
        Proceeds to load the CSV file and removing whitespaces ant the beginning and the end
        of the main file content.
        """
        self.csv_absolute_file_path = self.__get_path(input_source)
        if self.file_checker():
            self.csv_file = self.csv_opened.read().strip()

    def file_checker(self):
        """
        Loading files is considered a risky operation, so the code is wrapped in a
        try .. except block. (Maybe the file doesn't exist)
        """
        try:
            self.csv_opened = open(self.csv_absolute_file_path, "r")
            return True
        except IOError:
            raise IOError("The csv file does not appear to exist, exiting gracefully")
            return False

    def __get_path(self, input_source):
        """
        Private parameter that retrieves the full path of the CSV file by appending the Project
        absolute path and the CSV file relative path, it should generate a valid path independent
        of the OS.
        Keyword arguments:
        input_source -- Relative path of the CSV file
        Returned parameters:
        abs_file_path -- absolute path to the CSV file, performed thanks to os.path.join method.
         """
        abs_file_path = ""
        if os.path.isabs(input_source):
            abs_file_path = input_source
        else:
            file_path = os.path.normpath(input_source)
            abs_file_path = os.path.join(settings.root_path, file_path)
        return abs_file_path

    def save_file(self, output=None, data=None):
        """
        Not implemented yet
        """
        pass

    def retrieve_csv_grid(self):
        """
        Transform the standard csv content to a long string of 81 character without commas.
        """
        self.csv_file = self.csv_file.translate(None, ',')
        return self.csv_file
