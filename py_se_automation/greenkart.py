import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

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

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # hides Chromium logs


driver = Chrome(chrome_options)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()

# variables
veggies = ['Brocolli', 'Tomato', 'carrot']

# locators
add_to_cart = "//div[@class = 'product'][contains(., '<veggie-item>')]//button[text() = 'ADD TO CART']"
added_to_cart = "//div[@class = 'product'][contains(., '<veggie-item>')]//button[contains(text(), 'ADDED']"
locator_product_name = "//h4[@class = 'product-name']"
locator_cart = "//a[@class = 'cart-icon']"
locator_cart_items = "//ul[@class = 'cart-items]/li"
locator_item_price_each = "//div[contains(@class,'cart-preview')]//ul[@class = 'cart-items']/li//p[@class='amount']"

# functions
def wait_for_element(xpath, timeout = 20, retry = 3):
    wait = WebDriverWait(driver, timeout)
    for _ in range(retry):
        try:
            wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
            wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
        except RETRY_EXCEPTIONS:
            continue
    raise TimeoutException(f"Element not stable or interactable: {xpath}")
    
def find_element_by_xpath(xpath):
    driver.implicitly_wait(10)
    wait_for_element(xpath)
    return driver.find_element(By.XPATH, xpath)

def find_elements_by_xpath(xpath):
    driver.implicitly_wait(10)
    wait_for_element(xpath)
    return driver.find_elements(By.XPATH, xpath)

def click_element(xpath):
    wait_for_element(xpath)
    find_element_by_xpath(xpath).click()

def get_prods():
    products_elements = driver.find_elements(By.XPATH, locator_product_name)
    return products_elements

def get_prod_name():
    product_elements = get_prods()
    product_names = {product.text.split(' - ')[0] for product in product_elements}
    return product_names

def test_add_items_to_cart():
    {find_element_by_xpath(add_to_cart.replace('<veggie-item>', item_name)).click() for item_name in {product.text for product in get_prods() if product.text.split(' - ')[0].lower() in veggies or product.text.split(' - ')[0] in veggies}}

    item_names = {item_name for item_name in {product.text for product in get_prods() if product.text.split(' - ')[0].lower() in veggies or product.text.split(' - ')[0] in veggies}}

    for item_name in item_names:
        assert find_element_by_xpath(add_to_cart.replace('<veggie-item>', item_name)).is_displayed(), f'{item_name} not added to cart'
    
def test_validate_cart():
    test_add_items_to_cart()
    click_element(locator_cart)
    cart_price_elements = find_elements_by_xpath(locator_item_price_each)
    cart_price = {int(price_element.text) for price_element in cart_price_elements}
    print(cart_price)
    cart_total = sum(cart_price)
    print(cart_total)
