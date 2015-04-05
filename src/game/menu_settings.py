# menu_settings.py
from ..handlers.file_handler import FileHandler
from ..handlers.xml_handler import XMLHandler

class MenuSettings(object):
	def __init__(self):
		#print 'Subclass:', issubclass(XMLHandler, FileHandler)
  		#print 'Instance:', isinstance(XMLHandler(), FileHandler)
  		xml_file = XMLHandler()
   		xml_file.load_file("config\game_settings.xml")
   		print("============================================================")
   		print("=================CURRENT CONFIGURATION======================")
   		print("============================================================")
   		print "Current level: " + (xml_file.read_default_active_setting('level'))
   		print "Current algorithm: " + (xml_file.read_default_active_setting('algorithm'))
   		print "Current game output: " + (xml_file.read_child_active_settings('output','path'))
   		print "Current filename: " + (xml_file.read_child_active_settings('output','filename'))

		print("============================================================")
   		print("======================Select a LEVEL========================")
   		print("============================================================")
   		print(xml_file.read_all_settings('level'))		
   		my_level_list=xml_file.save_all_settings_into_array('level')	
   		correct_level=True
   		while correct_level:
   			level_type = raw_input("Write a level to be used:")
   			if level_type in my_level_list:
   				xml_file.define_default_active_setting("level",level_type)
   				xml_file.save_file()
   				correct_level=False
   			else:
   				print("Not valid level try again")	
   		
   		print("============================================================")
   		print("===================Select a ALGORITHM=======================")
   		print("============================================================")
   		print(xml_file.read_all_settings('algorithm'))
   		my_algorithm_list=xml_file.save_all_settings_into_array('algorithm')
   		correct_algorithm=True
   		while correct_algorithm:
   			algorithm_type = raw_input("Write a algorithm  to be used:")
   			if algorithm_type in my_algorithm_list:
   				xml_file.define_default_active_setting("algorithm",algorithm_type)   
   				xml_file.save_file()
   				correct_algorithm=False
   			else:
   				print("Not valid algorithm try again")
		
		print("============================================================")
   		print("=================Enter a new OUTPUT PATH====================")
   		print("============================================================")
   		#print(xml_file.read_all_settings('algorithm'))
   		output_path = raw_input("Write the output path :")
   		xml_file.change_text_fields("output","Game Output","path",output_path)
   		xml_file.save_file()

		print("============================================================")
   		print("===================Enter a FILE NAME========================")
   		print("============================================================")
   		#print(xml_file.read_all_settings('algorithm'))
   		file_name = raw_input("Write the File Name :")
   		xml_file.change_text_fields("output","Game Output","filename",file_name)
   		xml_file.save_file()
   	