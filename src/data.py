from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def set_default_email(driver):
    email_input = driver.find_element(By.XPATH, "//input[@type='text']")
    email_input.send_keys("5957099@gmail.com")


def set_default_password(driver):
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys("8j56t9")


def set_small_password(driver):
    small_password = driver.find_element(By.XPATH, "//input[@type='password']")
    small_password.send_keys("980")


def get_name():
    return 'Gamlet'
