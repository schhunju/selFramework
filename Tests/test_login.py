from datetime import time

import pytest

from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class TestLogin(BasePage):
    def test_login(self):
        try:
            # hello tester 123
            self.login = LoginPage(self.driver)
            self.login.logger.error("momo khana jam")
            self.login.enterFirstName("Nirjala")
            assert "dashboard" in self.driver.title
            time.sleep(5)
        except Exception as e:
            print(str(e))
