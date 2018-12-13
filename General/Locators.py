__author__ = 'Ricardo Acosta'


class Locators(object):

    # Login page locator
    login_title_x = "//h2[contains(string(), 'Login Panel')]"
    login_email_css = "input[type='text'][name='email']"
    login_password_css = "input[type='password']"
    login_button_css = "button[type='submit']"

    # Home page
    home_title_x = "//strong[contains(string(), 'Dashboard')]"
    # home_accounts_x = "ul[id='ACCOUNTS']"
    # home_accounts_x = "#ACCOUNTS"
    # home_customers_css = "a[href='https://www.phptravels.net/admin/accounts/customers/']"
    home_accounts_x = "//ul[@id='ACCOUNTS']/.."
    home_customers_css = "[href$='/customers/']"

