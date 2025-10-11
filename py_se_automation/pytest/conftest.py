import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-notifications")


    driver = Chrome(chrome_options)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.maximize_window()

    yield driver

    driver.quit()