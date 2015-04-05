"""This module is in charge of managing the basic I/O functionality required to setting up properly the XML file for the Sudoku2015-C game"""
import abc
import os
import xml.etree.ElementTree as ET
from file_handler import FileHandler
from ..settings import settings

class XMLHandler(FileHandler):
	""" 
	This derived class is based on the "FileHandler" base class which had abstract methods: load_file and save_file that will be fully implemented here.
	The "xml.etree.ElementTree" python module is being used in order to perform the XML data manipulation
	"""

	def __init__(self):
		"""The __init__ class method basically just initializes the xml_tree, xml_root, and xml_absolute_file_path variables to None because they are going to be defined in load_file method
		"""
		self.xml_tree = None
		self.xml_root = None
		self.xml_absolute_file_path = None

	def load_file(self, input_source = "config\game_settings.xml"):
		"""
		This method needed to be defined, otherwise a missing abstract method instantiation error would have been thrown by ABC metaclass.
		Basically is in charge of reading the XML default file from disk, by default the file should be located in "Sudoku2015-C\config\game_settings.xml" path. but only the relative path config\game_settings.xml can be provided, even no parameter can be set cause the optional parameter has the default path assigned
		"""
		self.xml_absolute_file_path = self._get_path(input_source)
		self.xml_tree = ET.parse(self.xml_absolute_file_path)
		self.xml_root = self.xml_tree.getroot()

	def save_file(self, output=None, data=None):
		"""
		This method needed to be defined, otherwise a missing abstract method instantiation error would have been thrown by ABC metaclass. 
		It has two optional parameters which take same default values of laod_file method if they are not provided by the user and then uses the write method of ET library 
		"""
		if output is None:
			output = self.xml_absolute_file_path

		if data is None:
			data = self.xml_root

		self.xml_tree = ET.ElementTree(self.xml_root)
		self.xml_tree.write(self.xml_absolute_file_path,"UTF-8")

	def _get_path(self, input_source):
		"""Private parameter that retrieves the full path of the XMl file by appedning the Project absolute path and the XML relative path, it should generate a valid path indepent of the OS"""
		file_path = os.path.normpath(input_source)
		abs_file_path = os.path.join(settings.root_path, file_path)
		return abs_file_path

	def define_default_active_setting(self, xml_tag , xml_attrib):
		"""This method allows XML settings file to be manipulated by modifying the "active" attribute to true in the "tag" defined and the remaining tags will have their attributes set to false   """
		for element in self.xml_root.iter(xml_tag):
			if element.attrib["name"] == xml_attrib:
				element.set("active","true")
			else:
				element.set("active","false")

	def retrieve_tag_summary(self, xml_tag):
		"""This method returns a summary of active values for all tags with the same "xml_tag" name """
		tag_summary = []
		for element in self.xml_root.iter(xml_tag):
			tag_summary.append({})
			if tag_summary and 'name' in element.attrib.keys():
   				tag_summary[-1][element.attrib['name']] = element.attrib['active']
   		return tag_summary

	def read_default_active_setting(self, xml_tag="ALL"):
		"""This method allows XML settings file to be manipulated by modifying the "active" attribute to true in the "tag" defined and the remaining tags will have their attributes set to false   """
		default_setting = None
		for element in self.xml_root.iter(xml_tag):
			if str(element.attrib["active"]) == "true":
				default_setting = str(element.attrib["name"])
		return default_setting

	def change_text_fields(self, parent_tag , name, child_tag, new_value):
		for element in self.xml_root.iter(parent_tag):
				if element.attrib["name"] == name:
					child = element.find(str(child_tag))
					child.text = str(new_value) 

	# def printData(self):
	# 	for element in self.xml_tree.iter():
	# 		print element.tag, element.attrib



	


	

