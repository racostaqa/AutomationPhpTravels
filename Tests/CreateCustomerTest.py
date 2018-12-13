__author__ = 'Ricardo'

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from General.Locators import Locators
from General.EnvironmentSetUp import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Data.Data import Data
import unittest


class CreateCustomerTest(EnvironmentSetup):

    def test_01_login(self):

        print("Navigating to Login Page")
        self.driver.get(Data.PHP_TRAVELS_WEB_ADDRESS)
        self.driver.maximize_window()

        # waiting for Title element to be present
        title_element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, Locators.login_title_x)))

        login_page = LoginPage(self.driver)
        login_page.set_title(title_element)

        # is_login_page_loaded = login_page.get_title().is_displayed()
        self.assertTrue(login_page.get_title().is_displayed())
        print("Login page is displayed")

        # entering credentials
        login_page.fill_email(Data.LOGIN_ADMIN_EMAIL)
        login_page.fill_password(Data.LOGIN_VALID_PASSWORD)
        print("Username and password entered")

        # clicking on submit button
        login_page.submit()
        print("Login in process...")

    def test_02_create_customer(self):
        home_page = HomePage(self.driver)
        # is_home_page_loaded = home_page.get_title().is_displayed()
        self.assertTrue(home_page.get_title().is_displayed())
        # self.assertTrue(is_login_page_loaded and is_home_page_loaded, "Login Page or Home page couldn't be loaded")
        print("Login successful")
        print("Home page is displayed")

        # Browse to Create customer page
        print("Navigating to Create Customer page")

        home_page.click_accounts()

        # waiting for Customers element to be enable
        customers_element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.home_customers_css)))
        home_page.set_customers(customers_element)

        home_page.click_customers()

        # verify Customer page is displayed

        # fill required fields, ect...

        # submit form

        # assert

        # Test completed
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
