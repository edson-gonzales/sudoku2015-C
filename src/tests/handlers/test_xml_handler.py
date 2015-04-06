"""
This module is in charge of testing the basic I/O functionality required to setting up properly the XML file 
for the Sudoku2015-C game
"""

import unittest

from ...handlers.xml_handler import XMLHandler

class TestXMLHandler(unittest.TestCase):

	def test_hard_level_change_is_properly_saved(self):
		xml = XMLHandler()
		xml.load_file()
		xml.define_default_active_setting("level", "Hard")
		xml.save_file()
		self.assertEquals("Hard", xml.read_default_active_setting('level'))

	def test_brute_force_algorithm_change_is_properly_saved(self):
		xml = XMLHandler()
		xml.load_file()
		xml.define_default_active_setting("level", "Hard")
		xml.define_default_active_setting("algorithm", "Brute Force")
		xml.save_file()
		self.assertEquals("Brute Force", xml.read_default_active_setting('algorithm'))

	def test_default_active_setting_for_levels_is_properly_saved(self):
		xml = XMLHandler()
		xml.load_file()
		xml.define_default_active_setting("level", "Medium")
		xml.save_file()
		summary_of_medium_active = [{'Easy': 'false'}, {'Medium': 'true'}, {'Hard': 'false'}, {'Custom': 'false'}]
		self.assertEquals(summary_of_medium_active, xml.retrieve_tag_summary("level"))

		xml.define_default_active_setting("level","Easy")
		xml.save_file()
		summary_of_easy_active = [{'Easy': 'true'}, {'Medium': 'false'}, {'Hard': 'false'}, {'Custom': 'false'}]
		self.assertEquals(summary_of_easy_active, xml.retrieve_tag_summary("level"))

	def test_default_active_setting_for_algorithms_is_properly_saved(self):
		xml = XMLHandler()
		xml.load_file()
		xml.define_default_active_setting("algorithm","Backtracking")
		xml.save_file()
		summary_of_backtracking_active = [{'Backtracking': 'true'}, {'Peter Novig': 'false'}, {'Brute Force': 'false'}]
		self.assertEquals(summary_of_backtracking_active, xml.retrieve_tag_summary("algorithm"))

		xml.define_default_active_setting("algorithm", "Peter Novig")
		xml.save_file()
		summary_of_peter_novig_active = [{'Backtracking': 'false'}, {'Peter Novig': 'true'}, {'Brute Force': 'false'}]
		self.assertEquals(summary_of_peter_novig_active, xml.retrieve_tag_summary("algorithm"))

	def test_range_of_missing_numbers_per_level(self):
		xml = XMLHandler()
		xml.load_file()
		xml.change_text_fields("level", "Easy", "min", "9")
		xml.save_file()
		self.assertEquals(str(9),xml.retrieve_text_node_value("level", "Easy", "min"))
		xml.change_text_fields("level", "Easy", "max", "20")
		xml.save_file()
		self.assertEquals(str(20),xml.retrieve_text_node_value("level", "Easy", "max"))

	def test_output_path_changes(self):
		xml = XMLHandler()
		xml.load_file()
		xml.change_text_fields("output", "Output Game", "path", "content/user/")
		xml.save_file()
		self.assertEquals("content/user/", xml.retrieve_text_node_value("output", "Game Output", "path"))


if __name__ == '__main__':
    unittest.main()