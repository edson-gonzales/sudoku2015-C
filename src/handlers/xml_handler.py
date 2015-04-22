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

  def load_file(self, input_source="config/game_settings.xml"):
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

    self.xml_tree = ET.ElementTree(data)

    try:
      self.xml_tree.write(output, "UTF-8")
    except Exception:
      print "Unexpected error writing to file %s" % (output)

  def __get_path(self, input_source):
    """
    Private parameter that retrieves the full path of the XMl file by appending the Project
    absolute path and the XML relative path, it should generate a valid path independent
    of the OS.
    Keyword arguments:
    input_source -- Relative path of the XML file
    Returned parameters:
    abs_file_path -- absolute path to the XML file, performed thanks to os.path.join method 
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

  def read_active_value_for_setting(self, xml_tag, name):
    """
    This method returns the "active" attribute value for the tag which a certain name
    Keyword arguments:
    xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
    name -- attribute name (i.e. name = Easy) from which the search will be even more specific
    Returned parameters:
    active_value -- active attribute value for the tag whith the name.
    """
    active_value = ""
    for element in self.xml_root.iter(xml_tag):
      if str(element.attrib["name"]) == name:
        active_value = str(element.attrib["active"])
    return active_value

  def read_default_active_setting(self, xml_tag):
    """
    This method returns the current tag name that has "active" attribute set to true
    Keyword arguments:
    xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down
    Returned parameters:
    default_setting -- current tag name that has "active" attribute set to true.
    """
    default_setting = ""
    for element in self.xml_root.iter(xml_tag):
      if str(element.attrib["active"]) == "true":
        default_setting = str(element.attrib["name"])
    return default_setting

  def change_text_fields(self, parent_tag, name, child_tag, new_value):
    """This method is able to set text node values in second level tags like min, max, filename
    and path.
    Keyword arguments:
    parent_tag -- parent tag name (i.e. level, algorithm) from which the search will be started.
    name -- attribute name (i.e. level name = Easy) from which the search will be narrowed down.
    child_tag -- child tag name (i.e. min, path) for setting up there new_value text node.
    new_value -- the text value that will be set in the child_tag.
    """
    for element in self.xml_root.iter(parent_tag):
      if element.attrib["name"] == name:
        child = element.find(str(child_tag))
        child.text = str(new_value)

  def read_options_per_tag(self, xml_tag):
    """This method returns an array of options that will be used for Settings Module
    Keyword arguments:
    xml_tag -- tag name (i.e. level, algorithm) from which the search will be narrowed down.
    Returned parameters:
    options -- array of all xml tags with a certain attribute name.
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
    Returned parameters:
    default_setting -- node text value of the child tag.
    """
    default_setting = ""
    for element in self.xml_root.iter(parent_tag):
      default_setting = element.find(str(child_tag)).text
    return default_setting

  def retrieve_text_node_value(self, parent_tag, name, child_tag):
    """This method allows to retrieve child tag values configured into XML settings file for
    a specific parent tag with a certain name attribute.
    Keyword arguments:
    parent_tag -- parent tag name (i.e. level, algorithm) from which the search will be started
    name -- attibute name (i.e. level name = Easy) from which the search will be narrowed down
    child_tag -- child tag name (i.e. min, path) for looking for an specific child tag
    Returned parameters:
    text -- node text value of the child tag with an specific name.
    """
    text = None
    for element in self.xml_root.iter(parent_tag):
      if element.attrib["name"] == name:
        text = (element.find(str(child_tag))).text
    return text     