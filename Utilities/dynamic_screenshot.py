import os
from selenium import webdriver
import time

class Screenshot:
    # Initialize the Screenshot class with driver
    def __init__(self, driver):
        self.driver = driver


    def take_screenshot(self, file_name: str):
        # Create a screenshots directory if it doesn't exist
        screenshots_dir = 'Tests/screenshots'
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Save the screenshot with a timestamp
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        screenshot_path = os.path.join(screenshots_dir, f'{file_name}_{timestamp}.png')

        # Save the screenshot
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
