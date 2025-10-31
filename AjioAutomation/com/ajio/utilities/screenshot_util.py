import os
import time
import re
from selenium.webdriver.remote.webdriver import WebDriver
from com.ajio.utilities.driver_manager import DriverManager

class ScreenshotUtil:
    @staticmethod
    def capture_screenshot(scenario_name: str) -> str:
        driver: WebDriver = DriverManager.get_driver()

        # Generate timestamped filename
        timestamp = time.strftime("%Y%m%d%H%M%S")
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', scenario_name)
        screenshot_name = f"{safe_name}_{timestamp}.png"
        screenshot_dir = os.path.join("test-output", "screenshots")
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        try:
            # Ensure directory exists
            os.makedirs(screenshot_dir, exist_ok=True)

            # Take screenshot and save
            driver.save_screenshot(screenshot_path)

        except Exception as e:
            print(f"Screenshot capture failed: {e}")

        return screenshot_path