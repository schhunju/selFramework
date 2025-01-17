import time
from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class TestLogin(BasePage):

    def test_login(self, base_url):
        LoginPage.googleSearch(self, base_url)