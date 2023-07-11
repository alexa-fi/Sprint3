import pytest
import random
from selenium import webdriver


@pytest.fixture(scope='function')
def chrome_browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.get('https://stellarburgers.nomoreparties.site/')
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture(scope='function')
def mail():
    email = str('5957099') + str(int(random.randint(100, 999))) + str('@gmail.com')
    return email