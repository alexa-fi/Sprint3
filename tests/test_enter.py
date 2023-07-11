from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
from locators import AuthorizationLocators
from locators import RegistrationLocators

class TestEnters:
    def test_enter_home_page_button_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            AuthorizationLocators.button_text_registration
        ))
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Авторизация не прошла'

    def test_enter_personal_account_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Личный кабинет не открылся'

    def test_enter_in_registration_form_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        chrome_browser.find_element(*AuthorizationLocators.button_text_registration).click()
        chrome_browser.find_element(*RegistrationLocators.button_text_enter).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Регистрация не прошла'

    def test_enter_in_reset_password_form_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.login_button).click()
        chrome_browser.find_element(*AuthorizationLocators.button_text_forgot_password).click()
        chrome_browser.find_element(*RegistrationLocators.button_text_enter).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        login_button = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        assert login_button.text == 'Оформить заказ', 'Сброс пароля не прошел'
