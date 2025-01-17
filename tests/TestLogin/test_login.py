import time
from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class TestLogin(BasePage):

    def test_login(self, base_url):

        self.login_page = LoginPage(self.driver)
        self.login_page.search_google(base_url, "abcd")
