import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
from locators import AuthorizationLocators
from locators import PersonalAccountLocators


class PersonalAreaToConstructor:
    def test_transition_sauses_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.sauces_button).click()
        sauce = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.sauce_third
        ))
        assert sauce.text == 'Соус традиционный галактический', 'Соус не найден'

    def test_transition_filling_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 20).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.filling_button).click()
        filling = WebDriverWait(chrome_browser, 20).until(EC.visibility_of_element_located(
            HomePageLocators.filling_second_ingredient
        ))
        assert filling.text == "Мясо бессмертных моллюсков Protostomia", 'Начинка не найдена'

    def test_transition_bulki_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.sauces_button).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.sauce_third
        ))
        chrome_browser.find_element(*HomePageLocators.bulki_button).click()
        bulka = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.bulki_second
        ))
        assert bulka.text == 'Краторная булка N-200i', 'Булка не найдена'

    def test_from_personal_account_to_constructor_construction_click_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            PersonalAccountLocators.text_change_personal_data
        ))
        chrome_browser.find_element(*PersonalAccountLocators.button_text_constructor_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.collect_burger_text
        ))
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))

    def test_go_construction_from_profile_logo_click_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        chrome_browser.find_element(*AuthorizationLocators.email_authorization).send_keys('5957099@gmail.com')
        chrome_browser.find_element(*AuthorizationLocators.password_authorization).send_keys('8j56t9')
        chrome_browser.find_element(*AuthorizationLocators.button_enter).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
        chrome_browser.find_element(*HomePageLocators.personal_account_button_text_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            PersonalAccountLocators.text_change_personal_data
        ))
        chrome_browser.find_element(*PersonalAccountLocators.button_text_constructor_header).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.collect_burger_text
        ))
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.place_order_button
        ))
