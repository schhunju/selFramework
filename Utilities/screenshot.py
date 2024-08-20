from selenium.webdriver.remote.webdriver import WebDriver

class ScreenshotUtil:

    @staticmethod
    def take_screenshot(driver: WebDriver, file_name: str):
        # Save the screenshot with the provided file name
        driver.save_screenshot(file_name)
        print(f"Screenshot saved as {file_name}")
