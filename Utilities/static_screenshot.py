import os
from selenium import webdriver
import time

class Screenshot:

    @staticmethod
    def take_screenshot(driver, file_name: str):
        # Create a screenshots directory if it doesn't exist
        screenshots_dir = 'Tests/screenshots'
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Save the screenshot with a timestamp
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        screenshot_path = os.path.join(screenshots_dir, f'{file_name}_{timestamp}.png')
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
