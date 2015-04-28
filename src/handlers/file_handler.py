#FileHandler.py
import abc

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