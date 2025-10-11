from utils.selenium_helpers import wait_for_element, click_element, find_element_by_xpath, find_elements_by_xpath
from selenium.webdriver.common.by import By

class ProductPage:
    locator_product_name = "//h4[@class='product-name']"
    add_to_cart = "//div[@class='product'][contains(., '<veggie-item>')]//button[text()='ADD TO CART']"
    locator_cart = "//a[@class='cart-icon']"
    locator_item_price_each = ("//div[contains(@class,'cart-preview')]"
                               "//ul[@class='cart-items']/li//p[@class='amount']")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return self.driver.find_elements(By.XPATH, self.locator_product_name)

    def add_items_to_cart(self, veggies):
        products = self.get_products()
        for product in products:
            name = product.text.split(' - ')[0]
            if name.lower() in [v.lower() for v in veggies]:
                click_element(self.driver, self.add_to_cart.replace('<veggie-item>', name))

    def open_cart(self):
        click_element(self.driver, self.locator_cart)

    def get_cart_prices(self):
        return {int(price.text) for price in find_elements_by_xpath(self.driver, self.locator_item_price_each)}