# menu_settings.py
from ..handlers.file_handler import FileHandler
from ..handlers.xml_handler import XMLHandler

class MenuSettings(object):
	def __init__(self):
		print 'Subclass:', issubclass(XMLHandler, FileHandler)
  		print 'Instance:', isinstance(XMLHandler(), FileHandler)
  		xml_file = XMLHandler()
   		xml_file.load_file("config\game_settings.xml")
   		print(xml_file.read_default_active_setting('level'))
		