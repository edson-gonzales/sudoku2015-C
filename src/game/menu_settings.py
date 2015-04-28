""" MenuSettings module basically just prints information that is managed by XML Handler"""
from menu_base import MenuBase
from ..handlers.file_handler import FileHandler
from ..handlers.xml_handler import XMLHandler
import time

class MenuSettings(MenuBase):
    def __init__(self):
        """ Loads the XML file and sets the order of the menu sections
        Note: This subclass is going to inherit useful and generic methods of MenuBase superclass
        """
        super(MenuSettings, self).__init__()
        self.current_response = None
        self.options = None
        self.range = [None] * 2
        self.xml_file = XMLHandler()
        self.xml_file.load_file()

    def show_settings_menu(self):
        """Prints the XML modification menus"""
        self.show_current_configuration()
        self.show_menu_level_settings()
        self.show_menu_algorithm_settings()
        self.show_menu_output_settings()

    def show_current_configuration(self):
        """Prints current XML configuration"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("CURRENT XML CONFIGURATION")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.__retrieve_xml_settings())

    def show_menu_level_settings(self):
        """Shows the level menu section"""
        print("\n~~~~~~~~~~~~~~")
        print("Select a Level")
        print("~~~~~~~~~~~~~~")
        section = 'level'
        self.define_menu_options(section)
        print(super(MenuSettings, self).build_multiple_options())
        if super(MenuSettings, self).validate_user_response():
            if self.options[self.current_response] == "Custom":
                print("\nLevel selected: 'Custom'. Saving and loading additional options...")
                time.sleep(2)
                self.__save_current_response(section)
                self.__show_menu_output_maximum_minimum_value()
                self.__show_menu_output_hint_value()

            else:       
                print("\nLevel selected: '%s'. Saving..." %(self.options[self.current_response]))
                time.sleep(2)
                self.__save_current_response(section)

    def show_menu_algorithm_settings(self):
        """Shows the algorithm menu section"""
        print("\n~~~~~~~~~~~~~~~~~~~")
        print("Select an Algorithm")
        print("~~~~~~~~~~~~~~~~~~~")
        section = 'algorithm'
        self.define_menu_options(section)
        print(super(MenuSettings, self).build_multiple_options())
        if super(MenuSettings, self).validate_user_response():
            print("\nAlgorithm selected: '%s'. Saving..." %(self.options[self.current_response]))
            time.sleep(2)
            self.__save_current_response(section)

    def __show_menu_output_maximum_minimum_value(self):
        """Shows the first custom level section: Range of visible numbers"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Set the range of visible numbers for 'Custom' level")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        section_min = 'min'
        section_max = 'max'
        tag_name = 'level'
        tag_value_name = 'Custom'
        if self.__validate_visible_range():
            print("\nSaving data...")
            time.sleep(2)
            self.__save_second_level_response(tag_name, tag_value_name, section_min, self.range[0])
            self.__save_second_level_response(tag_name, tag_value_name, section_max, self.range[1])

    def __validate_visible_range(self):
        """Validates minimum and maximum values for ranage of visible numbers"""
        is_response_max_min_valid = False
        while is_response_max_min_valid is False:
            min_value = super(MenuSettings, self).ask_user_input("Enter a valid minimum threshold")
            max_value = super(MenuSettings, self).ask_user_input("Enter a valid maximum threshold")
            if not (min_value.isdigit() and max_value.isdigit()):
                print("Not a number, please try again")
            elif (0 <= int(min_value) <= int(max_value)) and \
                (int(min_value) <= int(max_value) <= 81):
                is_response_max_min_valid = True
                self.range[0] = min_value
                self.range[1] = max_value
            else:
                print("Invalid range, please try again")
        return is_response_max_min_valid

    def __show_menu_output_hint_value(self):
        """Shows the hints menu section"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Set the maximum number of hints for 'Custom' level")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        section = 'hints'
        tag_nm = 'level'
        tag_value_nm = 'Custom'
        if super(MenuSettings, self).validate_correct_hint():
            print("\nSaving data...")
            time.sleep(2)
            self.__save_second_level_response(tag_nm, tag_value_nm, section, self.current_response)

    def show_menu_output_settings(self):
        """Shows both path and filename menu section"""
        self.__show_menu_output_path()
        self.__show_menu_output_filename()

    def __show_menu_output_path(self):
        """Shows path menu section"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Set a new relative 'path' for the output txt files")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        section = 'path'
        output_path = super(MenuSettings, self).ask_user_input("Enter a valid output path")
        tag_name = 'output'
        tag_value_name = 'Game Output'
        self.__save_second_level_response(tag_name, tag_value_name, section, output_path)
        print("Path: " + str(output_path) + " saved successfully as default output path")

    def __show_menu_output_filename(self):
        """Shows filename menu section"""
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Set a new file name pattern for the output txt files")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        section = 'filename'
        tag_name = 'output'
        tag_value_name = 'Game Output'
        file_name = super(MenuSettings, self).ask_user_input("Enter a valid file name")
        self.__save_second_level_response(tag_name, tag_value_name, section, file_name)
        print("File Name: " + str(file_name) + " saved successfully as default file name")

    def __retrieve_xml_settings(self):
        """ Provides a summary of all default current default options."""
        xml_settings = "Default level: "
        xml_settings += (self.xml_file.read_default_active_setting('level'))
        xml_settings += "\n" + "Default algorithm: "
        xml_settings += (self.xml_file.read_default_active_setting('algorithm'))
        xml_settings += "\n" + "Default output path: "
        xml_settings += (self.xml_file.retrieve_text_node_value('output', 'Game Output', 'path'))
        xml_settings += "\n" + "Default filename pattern: "
        xml_settings += (self.xml_file.retrieve_text_node_value('output', 'Game Output', 'filename'))
        xml_settings += "\n" + "\n" + "~~~~~~~~~ 'Custom' level configuration ~~~~~~~~~"
        xml_settings += "\n" + "Default minimum threshold for visible numbers: "
        xml_settings += (self.xml_file.retrieve_text_node_value('level', 'Custom', 'min'))
        xml_settings += "\n" + "Default maximum threshold for visible numbers: "
        xml_settings += (self.xml_file.retrieve_text_node_value('level', 'Custom', 'max'))
        xml_settings += "\n" + "Default maximum number of hints for user: "
        xml_settings += (self.xml_file.retrieve_text_node_value('level', 'Custom', 'hints'))
        return xml_settings

    def retrieve_default_settings(self):
        """ Provides a dictionary of all default current default options."""
        current_level = self.xml_file.read_default_active_setting('level')
        default_settings = {
            "level" : self.xml_file.read_default_active_setting('level'),
            "algorithm" : self.xml_file.read_default_active_setting('algorithm'),
            "path" : self.xml_file.retrieve_text_node_value('output', 'Game Output', 'path'),
            "filename" : self.xml_file.retrieve_text_node_value('output', 'Game Output', 'filename'),
            "min": self.xml_file.retrieve_text_node_value("level", current_level, "min"),
            "max": self.xml_file.retrieve_text_node_value("level", current_level, "max"),
            "hints": self.xml_file.retrieve_text_node_value("level", current_level, "hints"),
        }
        return default_settings

    def define_menu_options(self, tag_name):
        """ Returns a dictionary of all xml tag with a attrib name
        Keyword arguments:
        tag_name -- tag name (i.e. level, algorithm) from which all the xml tags will be retrieved.
        """
        self.options = self.xml_file.retrieve_dict_options_per_tag(tag_name)

    def __save_current_response(self, section):
        """" Save the settings for first level xml tags.
        Keyword arguments:
        section -- represents the section of the command line menu. (i.e. level, algorithm).
        """
        self.xml_file.define_default_active_setting(section, self.options[self.current_response])
        self.xml_file.save_file()

    def __save_second_level_response(self, tag_name, tag_value_name, section, response):
        """" Save the settings for second level "output" xml_tags.
        Keyword arguments:
        tag_name : root tag name of xml. e.g. level, algorithm or output
        tag_value_name : name to find an especific root tag. E.g. Easy to locate the first level.
        section -- represents a second level tag of tag_name (E.g. for level: min, max or hints).
        response -- value introduced by the user through the command line.
        """
        self.xml_file.change_text_fields(tag_name, tag_value_name, section, response)
        self.xml_file.save_file()
