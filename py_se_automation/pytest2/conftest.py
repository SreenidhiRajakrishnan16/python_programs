from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import pytest
import allure

@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--disable-notifications')

    driver = Chrome(chrome_options)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')

    yield driver

    driver.quit()