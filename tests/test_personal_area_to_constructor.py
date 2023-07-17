from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators


class TestPersonalAreaToConstructor:
    def test_transition_sauses_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.sauces_button).click()
        sauce = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(HomePageLocators.sauce_third))
        assert sauce.text == 'Соус традиционный галактический', 'Соус не найден'

    def test_transition_to_filling(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.filling_button).click()
        filling = WebDriverWait(chrome_browser, 10).until(
            EC.visibility_of_element_located(HomePageLocators.filling_second_ingredient))
        assert filling.text == 'Мясо бессмертных моллюсков Protostomia', 'Начинка не найдена'

    def test_transition_bulki_true(self, chrome_browser):
        chrome_browser.find_element(*HomePageLocators.sauces_button).click()
        WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.sauce_third
        ))
        chrome_browser.find_element(*HomePageLocators.bulki_button).click()
        bulka = WebDriverWait(chrome_browser, 10).until(EC.visibility_of_element_located(
            HomePageLocators.bulki_second
        ))
        assert bulka.text == 'Краторная булка N-200i', 'Булка не найдена'


