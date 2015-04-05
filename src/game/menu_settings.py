# menu_settings.py
from ..handlers.file_handler import FileHandler
from ..handlers.xml_handler import XMLHandler

class MenuSettings(object):
   def __init__(self):
      self.xml_file = XMLHandler()
      self.xml_file.load_file()
      self.print_current_configuration()
      self.print_level_settings()
      self.print_algorithm_settings()
      self.print_output_settings()

   def print_current_configuration(self):
      print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print ("~~~~~~~~~~~Welcome to the Sudoku2015-C game!~~~~~~~~~~~~~~~")
      print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("============================================================")
      print("=================CURRENT XML CONFIGURATION==================")
      print("============================================================")
      print "Current level: " + (self.xml_file.read_default_active_setting('level'))
      print "Current algorithm: " + (self.xml_file.read_default_active_setting('algorithm'))
      print "Current game output: " + (self.xml_file.read_child_active_settings('output','path'))
      print "Current filename: " + (self.xml_file.read_child_active_settings('output','filename'))

   def print_level_settings(self):
      print("============================================================")
      print("======================Select a LEVEL========================")
      print("============================================================")
      my_level_list=self.xml_file.read_options_per_tag('level')
      print(self._ask_multiple_options(my_level_list))   
      correct_level=True
      while correct_level:
         level_type = raw_input("Write a valid level name to be used:")
         if level_type in my_level_list:
            self.xml_file.define_default_active_setting("level",level_type)
            self.xml_file.save_file()
            correct_level=False
            print("Level: "+str(level_type) +" saved successfully as default option")  
         else:
            print("Not valid level, try again")  

   def print_algorithm_settings(self):
      print("============================================================")
      print("===================Select a ALGORITHM=======================")
      print("============================================================")
      my_algorithm_list=self.xml_file.read_options_per_tag('algorithm')
      print(self._ask_multiple_options(my_algorithm_list)) 
      correct_algorithm=True
      while correct_algorithm:
         algorithm_type = raw_input("Write a valid algorithm name  to be used:")
         if algorithm_type in my_algorithm_list:
            self.xml_file.define_default_active_setting("algorithm",algorithm_type)   
            self.xml_file.save_file()
            print("Algorithm: "+str(algorithm_type) +" saved successfully as default option")  
            correct_algorithm=False
         else:
            print("Not a valid algorithm, try again")

   def print_output_settings(self):
      print("============================================================")
      print("=================Enter a new OUTPUT PATH====================")
      print("============================================================")
      output_path = raw_input("Write the output path :")
      self.xml_file.change_text_fields("output","Game Output","path",output_path)
      self.xml_file.save_file()
      print("Path: "+str(output_path) +" saved successfully as default output path")  

      print("============================================================")
      print("===================Enter a FILE NAME========================")
      print("============================================================")
      file_name = raw_input("Write the File Name :")
      self.xml_file.change_text_fields("output","Game Output","filename",file_name)
      self.xml_file.save_file()
      print("Filename: "+str(file_name) +" saved successfully as default output filename") 

   def _ask_multiple_options(self, options):
      question = ""
      for index, option in enumerate(options):
          question =  question + "\n[" + str(index+1) + "] " + option
      question = question + "\n "
      return question
