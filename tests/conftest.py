import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def chrome_browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.get('https://stellarburgers.nomoreparties.site/')
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()
