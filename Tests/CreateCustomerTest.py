__author__ = 'Ricardo'

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.CustomerPage import CustomerPage
from Pages.AddCustomerPage import AddCustomerPage
from General.Locators import Locators
from General.EnvironmentSetUp import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Data.Data import Data
import unittest


class CreateCustomerTest(EnvironmentSetup):

    def test_01_login(self):

        print("Navigating to Login Page...")
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

        home_page = HomePage(self.driver)
        # is_home_page_loaded = home_page.get_title().is_displayed()
        self.assertTrue(home_page.get_title().is_displayed())
        # self.assertTrue(is_login_page_loaded and is_home_page_loaded, "Login Page or Home page couldn't be loaded")
        print("Login successful")

    def test_02_navigate_to_add_customer_page(self):
        home_page = HomePage(self.driver)
        # is_home_page_loaded = home_page.get_title().is_displayed()
        self.assertTrue(home_page.get_title().is_displayed())
        # self.assertTrue(is_login_page_loaded and is_home_page_loaded, "Login Page or Home page couldn't be loaded")
        print("Home page is displayed")

        # Browse to Create customer page
        print("Navigating to Add Customer page")

        home_page.click_accounts()

        # waiting for Customers element to be enable
        customers_element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, Locators.home_customers_css)))
        home_page.set_customers(customers_element)

        home_page.click_customers()

        customers_page = CustomerPage(self.driver)

        # waiting for Customers Management page to be enable
        customers_title_element = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locators.customers_title_x)))
        customers_page.set_customers_title(customers_title_element)

        # verify Customer page is displayed
        self.assertTrue(customers_page.get_customers_title().is_displayed())
        print("Customers Management page is displayed")

        # go to add customers page
        customers_page.click_add_customers_button()

        add_customers_page = AddCustomerPage(self.driver)
        # waiting for Add Customers page to be enable
        add_customers_title_element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, Locators.add_customers_title_x)))
        add_customers_page.set_add_customers_title(add_customers_title_element)

        # verify Add Customers page is displayed
        self.assertTrue(add_customers_page.get_add_customers_title().is_displayed())
        print("Add Customers page is displayed")

    def test_03_fill_inputs(self):
        # fill required fields
        add_customers_page = AddCustomerPage(self.driver)
        add_customers_page.fill_first_name(Data.CUSTOMER_FIRST_NAME)
        add_customers_page.fill_last_name(Data.CUSTOMER_LAST_NAME)
        add_customers_page.fill_email(Data.CUSTOMER_EMAIL)
        add_customers_page.fill_password(Data.CUSTOMER_PASSWORD)
        add_customers_page.fill_mobile(Data.CUSTOMER_MOBILE_NUMBER)
        add_customers_page.click_country_dropdown()
        add_customers_page.fill_country_input(Data.CUSTOMER_COUNTRY)
        add_customers_page.enter_country_input()
        add_customers_page.fill_address_1(Data.CUSTOMER_ADDRESS_1)
        add_customers_page.fill_address_2(Data.CUSTOMER_ADDRESS_2)
        add_customers_page.click_subscribe_checkbox()

        # submit form
        add_customers_page.click_submit_button()

    def test_04_check_created_user(self):
        customer_page = CustomerPage(self.driver)
        # waiting for Customers Page to be enable
        customers_title_element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, Locators.customers_title_x)))
        customer_page.set_customers_title(customers_title_element)
        # verify User was created
        self.assertTrue(customer_page.get_customers_title().is_displayed())
        print("Customers Management page is displayed again")

        self.assertTrue(customer_page.get_created_customer(Data.CUSTOMER_EMAIL).is_displayed())
        print("Customer " + Data.CUSTOMER_FIRST_NAME + " " + Data.CUSTOMER_LAST_NAME + " added successfully")

        # Test completed
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
