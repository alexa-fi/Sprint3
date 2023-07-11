from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import HomePageLocators
from tests.locators import AuthorizationLocators
from tests.locators import RegistrationLocators


class TestRegistration:
    def test_registration_user_true(self, chrome_browser, mail):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration)).click()
        chrome_browser.find_element(*RegistrationLocators.name_registration).send_keys('Gamlet')
        chrome_browser.find_element(*RegistrationLocators.email_registration).send_keys(mail)
        chrome_browser.find_element(*RegistrationLocators.password_registration).send_keys('8j56t9')
        chrome_browser.find_element(*RegistrationLocators.button_registration).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration))
        url = chrome_browser.current_url
        assert url == 'https://stellarburgers.nomoreparties.site/login'

    def test_incorrect_password_error(self, chrome_browser, mail):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(AuthorizationLocators.button_text_registration)).click()
        chrome_browser.find_element(*RegistrationLocators.name_registration).send_keys('Gamlet')
        chrome_browser.find_element(*RegistrationLocators.email_registration).send_keys(mail)
        chrome_browser.find_element(*RegistrationLocators.password_registration).send_keys('980')
        chrome_browser.find_element(*RegistrationLocators.button_registration).click()
        error_password = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            RegistrationLocators.wrong_password_text))
        assert error_password.text == 'Некорректный пароль'
