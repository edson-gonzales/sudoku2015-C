""" MenuFileExplorer module displays files with a certain extension 
to be loaded in the application"""
from menu_base import MenuBase
from ..settings import settings
from collections import OrderedDict
import fnmatch
import os
import time

class MenuFileExplorer(MenuBase):
    def __init__(self, extension):
        """ Initializes the most important parameters for looking for files of a certain
        extension and load them.
        Keyword arguments:
            extension -- file extension that will be used to filtered out the files contained
            in abs_input_path. (E.g. "csv", "txt" and so on)
        """
        super(MenuFileExplorer, self).__init__()
        self.options = None
        self.extension = extension
        self.current_response = None
        self.continue_file_menu = True
        self.file_menu_completed = False
        self.file_chosen = None
        self.abs_input_path = self.__get_path("content/sources")
        self.file_loop()

    def file_loop(self):
        """ Create a loop where the file menu can be displayed again if the user desires so.
        And also provides a friendly way to exit the file level
        """
        while self.continue_file_menu:
            self.show_file_explorer_menu()
            if self.continue_file_menu is False:
                break

    def show_file_explorer_menu(self):
        """
        Prints the available files of a certain extension and let use choose if they
        want to use our existing files or load another ones
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~ File explorer ~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Loading available '%s' files..."%(self.extension))
        time.sleep(2)
        self.retrieve_files_recursively()
        print(super(MenuFileExplorer, self).build_multiple_options()) 
        if len(self.options) > 0:
            question = '\nWould you like to use one of the existing files?'
            if super(MenuFileExplorer, self).eval_y_n(question):
                self.retrieve_user_response()
                self.continue_file_menu = False     
            else:
                self.manage_info_to_create_files()
        else:
            print("No files with the mentioned extension found...")
            self.manage_info_to_create_files()
        
    def retrieve_user_response(self):
        if super(MenuFileExplorer, self).validate_user_response():
            self.file_chosen = self.options[self.current_response]
            print("\nFile selected: '%s'. Executing...\n" %(self.file_chosen))
            time.sleep(2)

    def manage_info_to_create_files(self):
        """ Provides useful info to create valid files to be loaded to the application
            and then lead the user to the menu of avaialble files again to choose.
        """
        content_format = ""
        if self.extension == 'txt':
            content_format = "400000805\n030000000\n000700000\n020000060\n000080400\n000010000\n"+\
            "000603070\n500200000\n104000000\n"
        elif self.extension == 'csv':
            content_format = "003020600,900305001,001806400,008102900,700000008,006708200,"+\
            "002609500,800203009,005010300"
        else:
            content_format = "UNKNOWN"
        print("\nPlease create a '%s' file with content that follows this format:"%(self.extension))
        print(content_format)
        print("Where zeros represent empty spots.\n")
        print("Now save the file to this specific folder path:")
        print(self.abs_input_path)
        print("(You can also save the file to any folder inside the mentioned path)\n")
        if (super(MenuFileExplorer, self).eval_y_n("Press any key when the file is loaded")):
            self.show_file_explorer_menu()


    def retrieve_files_recursively(self):
        """Find all the files recursively with a certain extension,
        starting to look for them from abs_input_path path, and then store
        the search results in the options dictionary
        """
        matches = OrderedDict()
        index = 1
        for root, dirnames, filenames in os.walk(self.abs_input_path):
          for filename in fnmatch.filter(filenames, '*.' + self.extension):
            matches[str(index)] = os.path.join(root, filename)
            index += 1
        self.options = matches

    def __get_path(self, input_source):
        """
        Private parameter that retrieves the full path of the sources path for files by
        appending the Project absolute path and the relative source path, 
        it should generate a valid path independent of the OS.
        Keyword arguments:
        input_source -- Relative path of the sources path
        Returned parameters:
        abs_input_path -- absolute path to the sources path, performed thanks to os.path.join method 
         """
        file_path = os.path.normpath(input_source)
        abs_input_path = os.path.join(settings.root_path, file_path)
        return abs_input_path
