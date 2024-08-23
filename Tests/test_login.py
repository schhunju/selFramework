from datetime import time


from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage
from Utilities.screenshot import ScreenshotUtil


class TestLogin(BasePage):
    def test_login(self):
        try:
            self.login = LoginPage(self.driver)
            self.login.enterFirstName("Archana")
            assert "dashboard" in self.driver.title
            time.sleep(3)

            # take screenshot
            ScreenshotUtil.take_screenshot(self.driver, "login_screenshot.png")
        except Exception as e:
            print(str(e))
