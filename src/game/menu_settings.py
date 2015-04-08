""" MenuSettings module basically just prints information that is managed by XML Handler"""
from ..handlers.file_handler import FileHandler
from ..handlers.xml_handler import XMLHandler

class MenuSettings(object):
   def __init__(self):
      """ Loads the XML file and sets the order of the menu sections"""
      self.current_response = None
      self.xml_file = XMLHandler()
      self.xml_file.load_file()
      self.show_current_configuration()
      self.menu_level_settings()
      self.menu_algorithm_settings()
      self.menu_output_settings()

   def show_current_configuration(self):
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~Welcome to the Sudoku2015-C game!~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("============================================================")
      print("=================CURRENT XML CONFIGURATION==================")
      print("============================================================")
      print(self.__read_xml_settings())


   def menu_level_settings(self):
      print("============================================================")
      print("======================Select a LEVEL========================")
      print("============================================================")
      section = 'level'
      level_list = self.__read_xml_options(section)
      print(self.__show_multiple_options(level_list))
      if(self.__validate_user_response(level_list)):
         self.__save_current_response(section)
         print("Level: " +str(self.current_response) + " saved successfully as default option")


   def menu_algorithm_settings(self):
      print("============================================================")
      print("===================Select a ALGORITHM=======================")
      print("============================================================")
      section = 'algorithm'
      algorithm_list = self.__read_xml_options('algorithm')
      print(self.__show_multiple_options(algorithm_list))
      if(self.__validate_user_response(algorithm_list)):
         self.__save_current_response(section)
         print("Level: " + str(self.current_response) + " saved successfully as default option")

   def menu_output_settings(self):
      self.__menu_output_path()
      self.__menu_output_filename()

   def __menu_output_path(self):
      print("============================================================")
      print("=================Enter a new OUTPUT PATH====================")
      print("============================================================")
      section = 'path'
      output_path = self.__ask_user_input("Enter a valid output path")
      self.__save_current_output_response(section, output_path)
      print("Path: " + str(output_path) + " saved successfully as default output path")

   def __menu_output_filename(self):
      print("============================================================")
      print("===================Enter a FILE NAME========================")
      print("============================================================")
      section = 'filename'
      file_name = self.__ask_user_input("Enter a valid file name")
      self.__save_current_output_response(section, file_name)
      print("File Name: " + str(file_name) + " saved successfully as default file name")

   def __read_xml_settings(self):
      """ Provides a summary of all default current default options."""
      xml_settings = "Current level: "
      xml_settings += (self.xml_file.read_default_active_setting('level'))
      xml_settings += "\n" + "Current algorithm: "
      xml_settings += (self.xml_file.read_default_active_setting('algorithm'))
      xml_settings += "\n" + "Current game output: "
      xml_settings += (self.xml_file.read_child_active_settings('output', 'path'))
      xml_settings += "\n" + "Current filename: "
      xml_settings += (self.xml_file.read_child_active_settings('output', 'filename'))
      return xml_settings

   def __read_xml_options(self, tag_name):
      """ Returns an array of all xml tag with a attrib name
      Keyword arguments:
      tag_name -- tag name (i.e. level, algorithm) from which all the xml tags will be retrieved.
      """
      return self.xml_file.read_options_per_tag(tag_name)

   def __show_multiple_options(self, options):
      """ Provides a sorted menu of all xml tags of a certain type
      Keyword arguments:
      options -- array of all xml tags with a certain name attribute name.
      """
      question = ""
      for index, option in enumerate(options):
          question = question + "\n[" + str(index+1) + "] " + option
      question = question + "\n "
      return question

   def __validate_user_response(self, options):
      """" Evaluates the user response in a loop until a correct answer is set.
      Keyword arguments:
      options -- array of all xml tags with a certain attribute name.
      """
      is_response_valid = False
      while is_response_valid is False:
         response = self.__ask_user_input("Enter a valid option")
         if response in options:
            is_response_valid = True
            self.current_response = response
         else:
            print("Invalid option, please try again")

      return is_response_valid


   def __ask_user_input(self, sentence):
      """" Calls the python 2 raw_input method appending a colon character.
      Keyword arguments:
      sentence -- the question that eill be displayed in command line.
      """
      user_input = raw_input(sentence + " : ")
      return user_input

   def __save_current_response(self, section):
      """" Save the settings for first level xml tags.
      Keyword arguments:
      section -- represents the section of the command line menu. (i.e. level, algorithm).
      """
      self.xml_file.define_default_active_setting(section, self.current_response)
      self.xml_file.save_file()

   def __save_current_output_response(self, section, response):
      """" Save the settings for second level "output" xml_tags.
      Keyword arguments:
      section -- represents the second level section of the command line menu (i.e. path, filename).
      response -- value introduced by the user through the command line.
      """
      self.xml_file.change_text_fields("output", "Game Output", section, response)
      self.xml_file.save_file()


