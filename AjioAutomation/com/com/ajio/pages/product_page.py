from selenium.webdriver.common.by import By
from com.ajio.utilities.driver_manager import DriverManager

class ProductPage:
    def __init__(self):
        self.driver = DriverManager.get_driver()

    # Locators
    _first_product = (By.XPATH, "(//div[@class='item'])[1]")
    _add_to_cart = (By.XPATH, "//span[text()='ADD TO BAG']")

    # Actions
    def select_first_product(self):
        self.driver.find_element(*self._first_product).click()

    def add_to_cart(self):
        self.driver.find_element(*self._add_to_cart).click()