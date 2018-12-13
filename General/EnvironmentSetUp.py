__author__ = 'Ricardo Acosta'

import unittest
import datetime
from selenium import webdriver
from Data.Data import Data


class EnvironmentSetup(unittest.TestCase):

    driver = None

    # setUP contains the browser setup attributes
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(Data.CHROME_DRIVER_ADDRESS)
        print("Run Started at :" + str(datetime.datetime.now()))
        print("\n\n------------------------------------------------------------------")
        print("Chrome Environment Set Up\n")
        cls.driver.implicitly_wait(20)
        cls.driver.set_page_load_timeout(20)

    # tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            cls.driver.close()
            cls.driver.quit()
