import unittest
from com.ajio.utilities.base_test import BaseTest
from com.ajio.pages.login_page import LoginPage
from com.ajio.utilities.screenshot_util import ScreenshotUtil

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseTest.initialize_browser()

    def test_login_flow(self):
        login = LoginPage()
        login.click_sign_in()
        login.enter_email("test@example.com")
        login.click_continue()
        ScreenshotUtil.capture_screenshot("LoginFlow")

    @classmethod
    def tearDownClass(cls):
        BaseTest.quit_browser()