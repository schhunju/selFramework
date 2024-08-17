from datetime import time

import pytest

from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class TestLogin(BasePage):
    def test_login(self):
        try:
            # hello tester 123
            self.login = LoginPage(self.driver)
            self.login.logger.info("test_login started")
            self.login.enterFirstName("John")
            self.login.screenshot.take_screenshot(self.driver,"abcde")
            assert "DEMOQA" in self.driver.title
            time.sleep(5)

        except Exception as e:
            print(str(e))
