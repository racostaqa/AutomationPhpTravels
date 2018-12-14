__author__ = 'Ricardo Acosta'


class Locators(object):

    # Login page
    login_title_x = "//h2[contains(string(), 'Login Panel')]"
    login_email_css = "input[type='text'][name='email']"
    login_password_css = "input[type='password']"
    login_button_css = "button[type='submit']"

    # Home page
    home_title_x = "//strong[contains(string(), 'Dashboard')]"
    home_accounts_x = "//ul[@id='ACCOUNTS']/.."
    home_customers_css = "[href$='/customers/']"

    # Customer page
    customers_title_x = "//div[contains(string(), 'Customers Management')][@class='panel-heading']"
    add_customers_title_x = "//div[contains(string(), 'Add Customer')][@class='panel-heading']"
    customer_created = "//a[text()='{}']"

    # Add Customer page
    customer_add_button_css = "button[class='btn btn-success']"
    customer_first_name_css = "input[name='fname']"
    customer_last_name_css = "input[name='lname']"
    customer_email_css = "input[name='email']"
    customer_password_css = "input[name='password']"
    customer_mobile_number_css = "input[name='mobile']"
    customer_country_dropdown_css = "div[class='select2-container chosen-select']"
    customer_country_input_css = "input[type='text'][class='select2-input']"
    customer_address_1_css = "input[name='address1']"
    customer_address_2_css = "input[name='address2']"
    customer_email_subscriber_check_box_css = "ins[class='iCheck-helper']"
    customer_submit_button_css = "button[class='btn btn-primary']"
