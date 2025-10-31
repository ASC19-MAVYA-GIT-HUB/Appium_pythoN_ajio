from selenium.webdriver.common.by import By
from com.ajio.utilities.driver_manager import DriverManager

class HomePage:
    def __init__(self):
        self.driver = DriverManager.get_driver()

    # Locators
    _search_box = (By.NAME, "searchVal")
    _search_button = (By.CLASS_NAME, "search-button")

    # Actions
    def search_product(self, product_name):
        self.driver.find_element(*self._search_box).send_keys(product_name)
        self.driver.find_element(*self._search_button).click()