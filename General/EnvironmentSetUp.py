__author__ = 'Ricardo Acosta'

import unittest
import datetime
from selenium import webdriver
from Data.Data import Data


class EnvironmentSetup(unittest.TestCase):

    # setUP contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome(Data.CHROME_DRIVER_ADDRESS)
        print("Run Started at :"+str(datetime.datetime.now()))
        print("\n\n------------------------------------------------------------------")
        print("Chrome Environment Set Up\n")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # tearDown method just to close all the browser instances and then quit

    # def tearDown(self):
    #     if self.driver is not None:
    #         print("\nTest Environment Destroyed")
    #         print("----------------------------------------------------------")
    #         print("Run Completed at: " + str(datetime.datetime.now()))
    #         self.tearDown()
    #         self.driver.quit()
