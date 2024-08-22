from datetime import datetime
import time
from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage
from Utilities.screenshot import ScreenshotUtil



class TestLogin(BasePage):
    def test_login(self):
        try:
            # hello tester 123
            self.login = LoginPage(self.driver)
            self.login.logger.info("test_login started")
            self.login.enterFirstName("Ashmita")
            assert "DEMOQA" in self.driver.title

            # Create a dynamic screenshot filename using a timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_filename = f"login_screenshot_{timestamp}.png"

            # take screenshot
            ScreenshotUtil.take_screenshot(self.driver, screenshot_filename)

            time.sleep(5)

        except Exception as e:
            print(str(e))
