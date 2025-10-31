from selenium.webdriver.common.by import By
from com.ajio.utilities.driver_manager import DriverManager

class LoginPage:
    def __init__(self):
        self.driver = DriverManager.get_driver()

    # Locators
    _sign_in_button = (By.XPATH, "//span[text()='Sign In']")
    _email_input = (By.NAME, "username")
    _continue_button = (By.XPATH, "//button[text()='Continue']")

    # Actions
    def click_sign_in(self):
        self.driver.find_element(*self._sign_in_button).click()

    def enter_email(self, email):
        self.driver.find_element(*self._email_input).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self._continue_button).click()