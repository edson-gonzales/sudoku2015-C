"""Main file which is invoked tu run the program"""
from src.game.menu_settings import MenuSettings
from src.game.menu_main import MenuMain
from src.settings import settings


settings.init()
# menu = MenuSettings()
menu = MenuMain()




