import os
from datetime import datetime


class ScreenshotUtility:
    def __init__(self, driver, screenshot_folder="screenshots"):
        self.driver = driver
        self.screenshot_folder = screenshot_folder
        os.makedirs(self.screenshot_folder, exist_ok=True)

    def take_screenshot(self, name_prefix="screenshot"):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{name_prefix}_{timestamp}.png"
        screenshot_path = os.path.join(self.screenshot_folder, screenshot_name)
        self.driver.get_screenshot_as_file(screenshot_path)
        return screenshot_path
