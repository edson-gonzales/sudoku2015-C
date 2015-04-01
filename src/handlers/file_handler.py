#FileHandler.py
import abc
import os

class FileHandler(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def load_file(self, input_source):
		""" Retrieve Data from the input source and return an object """
		return 

	@abc.abstractmethod
	def save_file(self, output_source, data):
		""" Save the data object to the output """
		return

	def build_root_path(self):
		current_path = os.path.dirname(os.path.realpath(__file__))
		root_path = os.path.sep.join(current_path.split(os.path.sep)[:-2])
		return root_path


