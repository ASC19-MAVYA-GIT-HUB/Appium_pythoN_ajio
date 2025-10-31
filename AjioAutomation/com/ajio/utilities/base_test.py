import os
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.ajio.utilities.driver_manager import DriverManager

class BaseTest:
    driver = None
    prop = None

    @staticmethod
    def initialize_browser():
        try:
            # Load config.properties
            config_path = os.path.join("src", "test", "resources", "config.properties")
            BaseTest.prop = configparser.ConfigParser()
            BaseTest.prop.read(config_path)

            # Read browser type
            browser = BaseTest.prop.get("DEFAULT", "browser")

            # Setup Chrome
            if browser.lower() == "chrome":
                options = Options()
                service = Service()  # You can specify chromedriver path here if needed
                BaseTest.driver = webdriver.Chrome(service=service, options=options)
                DriverManager.set_driver(BaseTest.driver)

            # Apply timeouts
            BaseTest.driver.maximize_window()
            implicit_wait = int(BaseTest.prop.get("DEFAULT", "implicitWait"))
            page_load_timeout = int(BaseTest.prop.get("DEFAULT", "pageLoadTimeout"))

            BaseTest.driver.implicitly_wait(implicit_wait)
            BaseTest.driver.set_page_load_timeout(page_load_timeout)

            # Launch Ajio
            base_url = BaseTest.prop.get("DEFAULT", "baseUrl")
            BaseTest.driver.get(base_url)

        except Exception as e:
            print(f"❌ Error in BaseTest: {e}")

    @staticmethod
    def quit_browser():
        if BaseTest.driver:
            BaseTest.driver.quit()
            BaseTest.driver = None