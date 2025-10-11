from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    NoSuchElementException, 
    ElementNotVisibleException, 
    ElementNotInteractableException, 
    StaleElementReferenceException, 
    ElementClickInterceptedException,
    TimeoutException
    )

RETRY_EXCEPTIONS = (
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotVisibleException
)

def wait_for_element(driver, xpath, timeout=20, retry = 3):
    for _ in range(retry):
        try:
            wait = WebDriverWait(driver, timeout)
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
            wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
            return driver.find_element(By.XPATH, xpath)
        except RETRY_EXCEPTIONS:
            continue
    raise TimeoutException(f'Element not working/interactable after 3 tries')

def click_element(driver, xpath):
    element = wait_for_element(driver, xpath)
    element.click()

def find_element_by_xpath(driver, xpath):
    return wait_for_element(driver, xpath)

def find_elements_by_xpath(driver, xpath):
    return driver.find_elements(By.XPATH, xpath)