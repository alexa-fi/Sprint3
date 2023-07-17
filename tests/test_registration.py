from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import HomePageLocators
from tests.locators import AuthorizationLocators
from tests.locators import RegistrationLocators
from src.helpers import generate_email
from src import data
from src.data import get_name
from src.data import set_default_password
from src.data import set_small_password

email = generate_email()
name = get_name()


class TestRegistration:

    def test_registration_user_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration)).click()
        chrome_browser.find_element(*RegistrationLocators.name_registration).send_keys(name)
        chrome_browser.find_element(*RegistrationLocators.email_registration).send_keys(email)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*RegistrationLocators.button_registration).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration))
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys(email)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        check = login_button.text
        assert check == "Оформить заказ"

    def test_incorrect_password_error(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration)).click()
        chrome_browser.find_element(*RegistrationLocators.name_registration).send_keys(name)
        chrome_browser.find_element(*RegistrationLocators.email_registration).send_keys(email)
        set_small_password(chrome_browser)
        chrome_browser.find_element(*RegistrationLocators.button_registration).click()
        error_password = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            RegistrationLocators.wrong_password_text))
        assert error_password.text == 'Некорректный пароль'
