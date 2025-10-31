from threading import local
from selenium.webdriver.remote.webdriver import WebDriver

class DriverManager:
    _driver_storage = local()

    @staticmethod
    def get_driver() -> WebDriver:
        return getattr(DriverManager._driver_storage, "driver", None)

    @staticmethod
    def set_driver(driver_ref: WebDriver):
        DriverManager._driver_storage.driver = driver_ref

    @staticmethod
    def unload():
        if hasattr(DriverManager._driver_storage, "driver"):
            del DriverManager._driver_storage.driver