# menu_settings.py
import unittest

from ...game.menu_settings import MenuSettings

class TestMenuSettings(unittest.TestCase):
	"""
	Due to MenuSettings module basically just prints information that is managed by XML Handler, it was hard to find test scenarios to review using this test class, A comparison of strings is possible but first the MenuSettings  module needs to be refactored in order to store all the information in strings, arrays, or dictionaries to be compared here using "expected" variables and AssertEqual commmands
	"""
	def test_all_current_levels_should_be_displayed_when_printing_in_console(self):
		pass
		

if __name__ == '__main__':
    unittest.main()
		