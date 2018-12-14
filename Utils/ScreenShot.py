__author__ = 'Ricardo Acosta'
from Data.Data import Data


class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def take_screen_shot(self, path):
        directory = Data.SCREEN_SHOTS_DIRECTORY
        self.driver.get_screenshot_as_file(directory+path)

