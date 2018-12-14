__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.title = driver.find_element(By.XPATH, Locators.home_title_x)
        self.accounts = driver.find_element(By.XPATH, Locators.home_accounts_x)
        self.customers = driver.find_element(By.CSS_SELECTOR, Locators.home_customers_css)

    def get_title(self):
        return self.title

    def set_title(self, web_element):
        self.title = web_element

    def click_accounts(self):
        self.accounts.click()

    def set_accounts(self, web_element):
        self.accounts = web_element

    def click_customers(self):
        self.customers.click()

    def set_customers(self, web_element):
        self.customers = web_element

