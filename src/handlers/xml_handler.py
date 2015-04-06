"""
This module is in charge of managing the basic I/O functionality required to setting up 
properly the XML file for the Sudoku2015-C game
"""
import abc
import os
import xml.etree.ElementTree as ET
from file_handler import FileHandler
from ..settings import settings

class XMLHandler(FileHandler):
	""" 
	This derived class is based on the "FileHandler" base class which had abstract methods:
	load_file and save_file that will be fully implemented here.
	The "xml.etree.ElementTree" python module is being used in order to perform the XML data
	manipulation
	"""

	def __init__(self):
		"""
		The __init__ class method basically just initializes the xml_tree, xml_root, and 
		xml_absolute_file_path variables to None because they are going to be defined in load_file
		method
		"""
		self.xml_tree = None
		self.xml_root = None
		self.xml_absolute_file_path = None

	def load_file(self, input_source="config\game_settings.xml"):
		"""
		This method needed to be defined, otherwise a missing abstract method instantiation error 
		would have been thrown by ABC metaclass.
		Basically is in charge of reading the XML default file from disk, by default the file 
		should be located in "Sudoku2015-C\config\game_settings.xml" path. but only the relative 
		path config\game_settings.xml can be provided, even no parameter can be set cause the
		 optional parameter has the default path assigned.
		Keyword arguments:
		input_source -- relative path for accessing the XML file
		"""
		self.xml_absolute_file_path = self.__get_path(input_source)
		self.xml_tree = ET.parse(self.xml_absolute_file_path)
		self.xml_root = self.xml_tree.getroot()

	def save_file(self, output=None, data=None):
		"""
		This method needed to be defined, otherwise a missing abstract method instantiation error 
		would have been thrown by ABC metaclass. 
		It has two optional parameters which take same default values of laod_file method if they 
		are not provided by the user and then uses the write method of ET library.
		Keyword arguments:
		output -- relative path for writing the XML file 
		data -- XML info that will be written into the file
		"""
		if output is None:
			output = self.xml_absolute_file_path
		else:
			output = self.__get_path(output)

		if data is None:
			data = self.xml_root

		self.xml_tree.write(output, "UTF-8")

		try:
			self.xml_tree.write(output, "UTF-8")
		except Exception:
			print "Unexpected error writing to file %s" % (output)

	def __get_path(self, input_source):
		"""
		Private parameter that retrieves the full path of the XMl file by appedning the Project
		absolute path and the XML relative path, it should generate a valid path independent
		of the OS.
		Keyword arguments:
		data -- Relative path of the XML file
		 """
		file_path = os.path.normpath(input_source)
		abs_file_path = os.path.join(settings.root_path, file_path)
		return abs_file_path

	def define_default_active_setting(self, xml_tag, xml_attrib):
		"""
		This method allows XML settings file to be manipulated by modifying the "active"
		attribute to true in the "tag" defined and the remaining tags will have their
		attributes set to false.
		Keyword arguments:
		xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
		xml_attrib -- attribute name (i.e. level attrib = Easy) for setting up there "true" value 
		 """
		for element in self.xml_root.iter(xml_tag):
			if element.attrib["name"] == xml_attrib:
				element.set("active", "true")
			else:
				element.set("active", "false")

	def retrieve_tag_summary(self, xml_tag):
		"""This method returns a summary of active values for all tags with the same "xml_tag"
		name.
		Keyword arguments:
		xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
		"""
		tag_summary = []
		for element in self.xml_root.iter(xml_tag):
			tag_summary.append({})
			if tag_summary and 'name' in element.attrib.keys():
   				tag_summary[-1][element.attrib['name']] = element.attrib['active']
   		return tag_summary

	def read_default_active_setting(self, xml_tag):
		"""
		This method allows XML settings file to be manipulated by modifying the "active"
		attribute to true in the "tag" defined and the remaining tags will have their attributes
		set to false
		Keyword arguments:
		xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
		"""
		default_setting = ""
		for element in self.xml_root.iter(xml_tag):
			if str(element.attrib["active"]) == "true":
				default_setting = str(element.attrib["name"])
		return default_setting

	def change_text_fields(self, parent_tag, name, child_tag, new_value):
		"""
		This method is able to set text node values in second level tags like min, max, 
		filename and path.
		Keyword arguments:
		parent_tag -- parent tag name (i.e. level, algorithm) from which the search will be started
		name -- attibute name (i.e. level name = Easy) from which the search will be narrowed down
		child_tag -- child tag name (i.e. min, path) for setting up there new_value text node
		new_value -- the text value that will be set in the child_tag
		"""
		for element in self.xml_root.iter(parent_tag):
				if element.attrib["name"] == name:
					child = element.find(str(child_tag))
					child.text = str(new_value) 

	def read_options_per_tag(self, xml_tag):
		"""This method returns an array of options that will be used for Settings Module
		Keyword arguments:
		xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
		"""
		options = []
		for element in self.xml_root.iter(xml_tag):
				options.append(element.attrib["name"])
		return options

	def read_child_active_settings(self, parent_tag, child_tag):
		"""This method allows to retrieve child tag values configured into XML settings file
		Keyword arguments:
		parent_tag -- parent tag name (i.e. level, algorithm) from which the search will be started
		child_tag -- child tag name (i.e. min, path) for looking for an specific child tag
		"""
		default_setting = ""
  		for element in self.xml_root.iter(parent_tag):
   			default_setting = element.find(str(child_tag)).text
  		return default_setting

  	def retrieve_text_node_value(self, parent_tag, name, child_tag):
		"""This method allows to retrieve child tag values configured into XML settings file
		Keyword arguments:
		Keyword arguments:
		parent_tag -- parent tag name (i.e. level, algorithm) from which the search will be started
		name -- attibute name (i.e. level name = Easy) from which the search will be narrowed down
		child_tag -- child tag name (i.e. min, path) for looking for an specific child tag
		"""
		text = None
  		for element in self.xml_root.iter(parent_tag):
  			if element.attrib["name"] == name:
   				text = (element.find(str(child_tag))).text
  		return text
  	
			