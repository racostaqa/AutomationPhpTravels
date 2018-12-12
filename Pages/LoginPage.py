__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.title = driver.find_element(By.XPATH, Locators.login_title_x)
        self.email = driver.find_element(By.CSS_SELECTOR, Locators.login_email_css)
        self.password = driver.find_element(By.CSS_SELECTOR, Locators.login_password_css)
        self.button = driver.find_element(By.CSS_SELECTOR, Locators.login_button_css)

    def get_title(self):
        return self.title

    def set_title(self, web_element):
        self.title = web_element

    def fill_email(self, email):
        self.email.send_keys(email)

    def set_email(self, web_element):
        self.email = web_element

    def fill_password(self, password):
        self.password.send_keys(password)

    def set_password(self, web_element):
        self.password = web_element

    def submit(self):
        self.button.click()

    def set_button(self, web_element):
        self.button = web_element
