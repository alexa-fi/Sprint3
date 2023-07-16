from selenium.webdriver.common.by import By
from tests.locators import AuthorizationLocators
from tests.locators import RegistrationLocators


def set_default_email(driver):
    email_input = driver.find_element(*AuthorizationLocators.email_authorization)
    email_input.send_keys("5957099@gmail.com")


def set_default_password(driver):
    password_input = driver.find_element(*AuthorizationLocators.password_input)
    password_input.send_keys("8j56t9")


def set_small_password(driver):
    small_password = driver.find_element(*RegistrationLocators.small_password)
    small_password.send_keys("980")


def get_name():
    return 'Gamlet'
