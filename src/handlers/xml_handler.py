import abc
from file_handler import FileHandler
import os
import xml.etree.ElementTree as ET

class XMLHandler(FileHandler):

	def __init__(self):
		self.root_path = super(XMLHandler,self).build_root_path() 
		self.xml_tree = None
		self.xml_root = None

	def load_file(self, input_source):
		self.xml_tree = ET.parse(self._build_absolute_path(input_source))
		self.xml_root = self.xml_tree.getroot()
		# print(self.xml_tree)
		# return input.read()

	def _build_absolute_path(self, input_source):
		#xml_file_path = "config\settings.xml"
		xml_file_path = os.path.normpath(input_source)
		xml_abs_file_path = os.path.join(self.root_path, xml_file_path)
		return xml_abs_file_path

	def printData(self):
		for levels in self.xml_root.iter('levels'):
			print levels.attrib

		# for level in self.xml_root.findall('level'):
		# 	min = level.find('min').text
		# 	max = level.find('max').text
		# 	name = level.get('name')
		# 	print name
		# 	print min
		# 	print max

		for algorithms in self.xml_root.iter('algorithm'):
			print algorithms.attrib
		for output in self.xml_root.iter('output'):
			print output.attrib

	def save_file(self, output, data):
		return output.write(data)

	def read(self):
		pass

	



# if __name__ == '__main__':
#    print 'Subclass:', issubclass(XMLHandler, FileHandler)
#    print 'Instance:', isinstance(XMLHandler(), FileHandler)
#    XMLHandler().load_file("config\settings.xml")
