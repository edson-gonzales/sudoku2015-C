"""
This module is in charge of managing the basic I/O functionality required to setting up 
properly the TXT files for the Sudoku2015-C game
"""
import abc
import os
from file_handler import FileHandler
from ..settings import settings

class TXTHandler(FileHandler):
  """ 
  This derived class is based on the "FileHandler" base class which had abstract methods:
  load_file and save_file that will be fully implemented here.
  """

  def __init__(self):
    """ Defines the object attributes that will be used throughout this class."""
    self.txt_absolute_file_path = None
    self.txt_opened = None
    self.txt_file = None

  def load_file(self, input_source):
    """ 
    Proceeds to load the CSV file and removing whitespaces ant the beginning and the end
    of the main file content.
    """
    self.txt_absolute_file_path = self.__get_path(input_source)
    if self.file_checker():
      self.txt_file = self.txt_opened.read().strip()
      

  def file_checker(self):
    """
    Loading files is considered a risky operation, so the code is wrapped in a
    try .. except block. (Maybe the file doesn't exist)
    """
    try:
      self.txt_opened = open(self.txt_absolute_file_path, "r")
      return True
    except IOError:
      raise IOError("The txt file does not appear to exist, exiting gracefully")
      return False

  def __get_path(self, input_source):
    """
    Private parameter that retrieves the full path of the TXT file by appending the Project
    absolute path and the TXT file relative path, it should generate a valid path independent
    of the OS.
    Keyword arguments:
    input_source -- Relative path of the TXT file
    Returned parameters:
    abs_file_path -- absolute path to the TXT file, performed thanks to os.path.join method 
     """
    file_path = os.path.normpath(input_source)
    abs_file_path = os.path.join(settings.root_path, file_path)
    return abs_file_path

  def save_file(self, output=None, data=None):
    """
    Not implemented yet
    """
    pass

  def retrieve_txt_grid(self):
    """
    Transform the standard csv content to a long string of 81 character without line breaks.
    """
    self.txt_file = self.txt_file.translate(None, '\n')
    return self.txt_file



