# boilerplate to allow running as script directly

# from __future__ import absolute_import

# if __name__ == "__main__" and __package__ is None:
#     import sys, os
#     # The following assumes the script is in the top level of the package
#     # directory.  We use dirname() to help get the parent directory to add to
#     # sys.path, so that we can import the current package.  This is necessary 
#     # since when invoked directly, the 'current' package is not automatically
#     # imported.

#     parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.insert(1, parent_dir)
#     sudoku2015 = __import__("sudoku2015-C")
#     sys.modules["sudoku2015-C"] = sudoku2015
#     __package__ = str("sudoku2015-C")
#     del sys, os

# # now you can use relative imports here that will work regardless of how this
# # python file was accessed (either through 'import', through 'python -m', or 
# # directly.

from src.game.menu_settings import MenuSettings
from src.settings import settings


settings.init()
menu = MenuSettings()

# os.cmd   set PYTHONPATH


