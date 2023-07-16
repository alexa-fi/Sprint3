from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
from locators import AuthorizationLocators
from locators import PersonalAccountLocators
from src import data
from src.data import set_default_email
from src.data import set_default_password


class TestPersonalAccount:
    def test_go_to_personal_account_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        set_default_email(chrome_browser)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            PersonalAccountLocators.text_change_personal_data))
        url = chrome_browser.current_url
        assert url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_logout_from_personal_account_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        set_default_email(chrome_browser)
        set_default_password(chrome_browser)
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            PersonalAccountLocators.text_change_personal_data
        ))
        chrome_browser.find_element(*PersonalAccountLocators.logout_button).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            AuthorizationLocators.text_enter
        ))
        url = chrome_browser.current_url
        assert url == 'https://stellarburgers.nomoreparties.site/login'
