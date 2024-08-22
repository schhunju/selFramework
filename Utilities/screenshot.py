from selenium.webdriver.remote.webdriver import WebDriver
import os
class ScreenshotUtil:

    @staticmethod
    def take_screenshot(driver: WebDriver, file_name: str, screenshot_dir ="screenshots"):
        # Ensure the screenshot directory exists
        os.makedirs(screenshot_dir, exist_ok=True)

        # Create the full file path
        file_path = os.path.join(screenshot_dir, file_name)

        # Save the screenshot with the provided file name
        driver.save_screenshot(file_path)
        print(f"Screenshot saved as {file_path}")
