from datetime import time


from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage
from Utilities.screenshot import ScreenshotUtil


class TestLogin(BasePage):
    def test_login(self):
        try:
            # hello tester 123
            self.login = LoginPage(self.driver)
            self.login.enterFirstName("John")
            assert "dashboard" in self.driver.title
            time.sleep(5)

            # take screenshot
            ScreenshotUtil.take_screenshot(self.driver, "login_screenshot.png")
        except Exception as e:
            print(str(e))
