# from src.game.menu_settings import MenuSettings
import unittest
from src.settings import settings
from src.tests.handlers.test_xml_handler import TestXMLHandler

settings.init()

xml_suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLHandler)

alltests = unittest.TestSuite([xml_suite])

unittest.TextTestRunner(verbosity=1).run(alltests)
