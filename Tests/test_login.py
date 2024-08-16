from selFramework.Pages.Basepage import BasePage
from selFramework.Pages.LoginPage import LoginPage
from selFramework.Utilities.screenshot_utility import ScreenshotUtility


class TestLogin(BasePage):
    def test_login(self):
        try:
            self.login = LoginPage(self.driver)
            self.login.logger.error("momo khana jam")
            self.login.enterFirstName("John")
            assert "DEMOQA" in self.driver.title
            self.login.logger.info("Login test passed")
        except Exception as e:
            screenshot_util = ScreenshotUtility(self.driver)
            screenshot_path = screenshot_util.take_screenshot("login_error")
            self.login.logger.error(f"Login test failed. Screenshot saved at {screenshot_path}")
            self.login.logger.error(str(e))
            raise
