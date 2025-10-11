from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)

RETRY_EXCEPTIONS = (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
)

def wait_for_element(driver, xpath, timeout = 20, retry = 3):
    wait = WebDriverWait(driver, timeout)
    driver.implicitly_wait(10)
    for _ in range(retry):
        try:
            wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
            wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            return driver.find_element(By.XPATH, xpath)
        except RETRY_EXCEPTIONS:
            continue
    raise TimeoutException(f"Element not stable or interactable: {xpath}")

def click_element(driver, xpath):
    element = wait_for_element(driver, xpath)
    element.click()

def find_elements_by_xpath(driver, xpath):
    wait_for_element(driver, xpath)
    return driver.find_elements(By.XPATH, xpath)

def find_element_by_xpath(driver, xpath):
    wait_for_element(driver, xpath)
    return driver.find_element(By.XPATH, xpath)