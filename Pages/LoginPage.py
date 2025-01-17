from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    googleSearch = "//*[@name='q']"

    def invoke_browser(self, url):
        print(self.driver)
        self.driver.get(url)
        print(url)

    def search_google(self, url):
        self.invoke_browser(url)
        # BasePage.enter_text_into_element(self.googleSearch, search_text)
        # BasePage.clickElementByXpath(self, LoginPage.googleSearch)