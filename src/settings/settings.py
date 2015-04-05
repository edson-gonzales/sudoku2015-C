"""This module establishes the global variables that all the remaining modules related to Sudoku2015-C will be able to use."""
import os

def init():
	"""Return the pathname of the Sudoku2015-C directory"""
	global root_path 
	root_path = os.path.dirname(os.path.realpath(__file__))
	root_path = os.path.sep.join(root_path.split(os.path.sep)[:-2])