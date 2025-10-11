import allure
import pytest

from pages.products_page import ProductPage

from utils.selenium_helpers import find_elements_by_xpath

@allure.feature("Cart Functionality")
@allure.story("Add items and validate cart")
@pytest.mark.smoke
def test_cart_flow(driver):
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    veggies = ["Brocolli", "Tomato", "Carrot"]
    cart = ProductPage(driver)

    with allure.step("Add selected items to cart"):
        cart.add_items_to_cart(veggies)

    with allure.step("Open cart and validate prices"):
        cart.open_cart()
        prices = cart.get_cart_prices()
        total = sum(prices)
        allure.attach(str(prices), "Individual Item Prices", allure.attachment_type.TEXT)
        allure.attach(str(total), "Total", allure.attachment_type.TEXT)
        assert total > 0, "Cart total should be positive"
