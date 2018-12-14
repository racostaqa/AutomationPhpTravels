__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddCustomerPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.add_customers_title = driver.find_element(By.XPATH, Locators.add_customers_title_x)
        self.first_name = driver.find_element(By.CSS_SELECTOR, Locators.customer_first_name_css)
        self.last_name = driver.find_element(By.CSS_SELECTOR, Locators.customer_last_name_css)
        self.email = driver.find_element(By.CSS_SELECTOR, Locators.customer_email_css)
        self.password = driver.find_element(By.CSS_SELECTOR, Locators.customer_password_css)
        self.mobile_number = driver.find_element(By.CSS_SELECTOR, Locators.customer_mobile_number_css)
        self.country_dropdown = driver.find_element(By.CSS_SELECTOR, Locators.customer_country_dropdown_css)
        self.country_input = driver.find_element(By.CSS_SELECTOR, Locators.customer_country_input_css)
        self.address_1 = driver.find_element(By.CSS_SELECTOR, Locators.customer_address_1_css)
        self.address_2 = driver.find_element(By.CSS_SELECTOR, Locators.customer_address_2_css)
        self.subscribe_checkbox = driver.find_element(By.CSS_SELECTOR, Locators.customer_email_subscriber_check_box_css)
        self.submit_button = driver.find_element(By.CSS_SELECTOR, Locators.customer_submit_button_css)

    def get_add_customers_title(self):
        return self.add_customers_title

    def set_add_customers_title(self, web_element):
        self.add_customers_title = web_element

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, web_element):
        self.first_name = web_element

    def fill_first_name(self, text):
        self.first_name.send_keys(text)

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, web_element):
        self.last_name = web_element

    def fill_last_name(self, text):
        self.last_name.send_keys(text)

    def get_email(self):
        return self.email

    def set_email(self, web_element):
        self.email = web_element

    def fill_email(self, text):
        self.email.send_keys(text)

    def get_password(self):
        return self.password

    def set_password(self, web_element):
        self.password = web_element

    def fill_password(self, text):
        self.password.send_keys(text)

    def get_mobile(self):
        return self.mobile_number

    def set_mobile(self, web_element):
        self.mobile_number = web_element

    def fill_mobile(self, text):
        self.mobile_number.send_keys(text)

    def get_country_dropdown(self):
        return self.country_dropdown

    def set_country_dropdown(self, web_element):
        self.country_dropdown = web_element

    def click_country_dropdown(self):
        self.country_dropdown.click()

    def get_country_input(self):
        return self.country_input

    def set_country_input(self, web_element):
        self.country_input = web_element

    def fill_country_input(self, text):
        self.country_input.send_keys(text)

    def enter_country_input(self):
        self.country_input.send_keys(Keys.ENTER)

    def get_address_1(self):
        return self.address_1

    def set_address_1(self, web_element):
        self.address_1 = web_element

    def fill_address_1(self, text):
        self.address_1.send_keys(text)

    def get_address_2(self):
        return self.address_2

    def set_address_2(self, web_element):
        self.address_2 = web_element

    def fill_address_2(self, text):
        self.address_2.send_keys(text)

    def get_subscribe_checkbox(self):
        return self.subscribe_checkbox

    def set_subscribe_checkbox(self, web_element):
        self.subscribe_checkbox = web_element

    def click_subscribe_checkbox(self):
        self.subscribe_checkbox.click()

    def get_submit_button(self):
        return self.submit_button

    def set_submit_button(self, web_element):
        self.submit_button = web_element

    def click_submit_button(self):
        self.submit_button.click()

