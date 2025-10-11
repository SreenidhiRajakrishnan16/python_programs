import pytest

@pytest.fixture
def base_page(driver):
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    yield driver