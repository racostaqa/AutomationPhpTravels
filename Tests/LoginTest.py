__author__ = 'Ricardo'

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from General.Locators import Locators
from General.EnvironmentSetUp import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Data.Data import Data
from time import sleep
import unittest


class LoginTest(EnvironmentSetup):

    def test_set_up(self):
        # browser set up
        # self.setUp()
        self.driver.get(Data.PHP_TRAVELS_WEB_ADDRESS)
        self.driver.set_page_load_timeout(20)

    def test_login(self):

        # Screen shots
        # screen_shot_path = Data.LOGIN_SCREEN_SHOTS_PATH
        # screen_shot = ScreenShot(self.driver)
        # try:
        # -------------------
        # calling Google home page
        login_page = LoginPage(self.driver)

        # waiting for Title element to be present
        title_element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, Locators.login_title_x)))
        login_page.set_title(title_element)

        self.assertTrue(login_page.get_title().is_displayed())
        print("Login page is displayed")

        # entering credentials
        login_page.fill_email(Data.LOGIN_ADMIN_EMAIL)
        login_page.fill_password(Data.LOGIN_VALID_PASSWORD)

        # clicking on submit button
        login_page.submit()
        sleep(3)
        print("Login in process...")

        # verifying Login
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.get_title().is_displayed())
        print("Login successful")
        # Test completed
        print("Test completed")
        # ----------------
        # except AssertionError as error:
        #     print("Login failed.\nError: " + str(error))
        #     screen_shot.take_screen_shot(screen_shot_path+"login.png")
        #     # Test completed
        #     print("Test completed")
        #
        # except Exception as exception:
        #     print("Login failed.\nException: " + str(exception))
        #     screen_shot.take_screen_shot(screen_shot_path+"login.png")
        #     # Test completed
        #     print("Test completed")


if __name__ == '__main__':
    unittest.main()
