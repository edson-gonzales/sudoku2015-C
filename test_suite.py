# from src.game.menu_settings import MenuSettings
import unittest
from src.settings import settings
from src.tests.handlers.test_xml_handler import TestXMLHandler
from src.tests.game.test_menu_settings import TestMenuSettings

settings.init()

xml_suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLHandler)
menu_suite = unittest.TestLoader().loadTestsFromTestCase(TestMenuSettings)

alltests = unittest.TestSuite([xml_suite, menu_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)
