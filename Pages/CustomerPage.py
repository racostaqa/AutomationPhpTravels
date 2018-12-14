__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class CustomerPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.customers_title = driver.find_element(By.XPATH, Locators.customers_title_x)
        self.add_customer_button = driver.find_element(By.CSS_SELECTOR, Locators.customer_add_button_css)

    def get_customers_title(self):
        return self.customers_title

    def set_customers_title(self, web_element):
        self.customers_title = web_element

    def get_add_customers_button(self):
        return self.add_customer_button

    def set_add_customers_button(self, web_element):
        self.add_customer_button = web_element

    def click_add_customers_button(self):
        self.add_customer_button.click()

    def get_created_customer(self, email):
        element = Locators.customer_created.format(email)
        return self.driver.find_element(By.XPATH, element)

