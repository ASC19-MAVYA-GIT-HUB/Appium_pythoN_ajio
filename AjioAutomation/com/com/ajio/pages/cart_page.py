from selenium.webdriver.common.by import By
from com.ajio.utilities.driver_manager import DriverManager

class CartPage:
    def __init__(self):
        self.driver = DriverManager.get_driver()

    # Locators
    _cart_icon = (By.XPATH, "//span[text()='Bag']")
    _checkout_button = (By.XPATH, "//button[text()='Proceed to Checkout']")

    # Actions
    def open_cart(self):
        self.driver.find_element(*self._cart_icon).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self._checkout_button).click()