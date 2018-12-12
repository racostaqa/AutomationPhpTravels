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


class CreateCustomerTest(EnvironmentSetup):

    def test_01_login(self):
        # Using the driver instances created in EnvironmentSetup
        driver = self.driver
        self.driver.get(Data.PHP_TRAVELS_WEB_ADDRESS)
        self.driver.set_page_load_timeout(20)

        # calling Google home page
        login_page = LoginPage(driver)

        # waiting for Title element to be present
        title_element = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, Locators.login_title_x)))
        login_page.set_title(title_element)

        # is_login_page_loaded = login_page.get_title().is_displayed()
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
        home_page = HomePage(driver)
        # is_home_page_loaded = home_page.get_title().is_displayed()
        self.assertTrue(home_page.get_title().is_displayed())
        # self.assertTrue(is_login_page_loaded and is_home_page_loaded, "Login Page or Home page couldn't be loaded")
        print("Login successful")

    # def test_02_create_customer(self):
    #     # Browse to Create customer page
    #     home_page = HomePage(self.driver)
    #     home_page.click_accounts()
    #     sleep(3)
    #     home_page.click_customers()
    #     sleep(2)
    #
    #     # verify Customer page is displayed
    #
    #     # fill required fields, ect...
    #
    #     # submit form
    #
    #     # assert
    #
    #     # Test completed
    #     print("Test completed")


if __name__ == '__main__':
    unittest.main()
