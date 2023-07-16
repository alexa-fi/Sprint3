from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
from locators import AuthorizationLocators
from locators import RegistrationLocators
from src import data
from src.data import set_default_email
from src.data import set_default_password


class TestEnters:
    def test_enter_home_page_button_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            AuthorizationLocators.button_text_registration
        ))
        set_default_email(chrome_browser)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Авторизация не прошла'

    def test_enter_personal_account_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        data.set_default_email(chrome_browser)
        data.set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Личный кабинет не открылся'

    def test_enter_in_registration_form_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        chrome_browser.find_element(*AuthorizationLocators.button_text_registration).click()
        chrome_browser.find_element(*RegistrationLocators.button_text_enter).click()
        set_default_email(chrome_browser)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Регистрация не прошла'

    def test_enter_in_reset_password_form_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        chrome_browser.find_element(*AuthorizationLocators.button_text_forgot_password).click()
        chrome_browser.find_element(*RegistrationLocators.button_text_enter).click()
        set_default_email(chrome_browser)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Сброс пароля не прошел'
