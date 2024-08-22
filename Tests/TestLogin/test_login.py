import time
from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class TestLogin(BasePage):
    def test_login(self):
        try:
            # hello tester 123
            self.login = LoginPage(self.driver)
            self.login.logger.info("test_login started")
            self.login.enterFirstName("John")
            #calling the take_screenshot method from Screenshot class by passing the filename
            self.login.screenshot.take_screenshot("abcde")
            assert "DEMOQA" in self.driver.title
            time.sleep(2)

        except Exception as e:
            print(str(e))
