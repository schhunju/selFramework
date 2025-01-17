from selenium.webdriver import Keys

from Pages.Basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    input_search = "//*[@name='q']"

    def invoke_browser(self, url):
        print(self.driver)
        self.driver.get(url)
        print(url)

    def search_google(self, url, search_text):
        self.invoke_browser(url)
        self.enter_text_into_element(self.input_search, search_text)
        self.enter_text_into_element(self.input_search, Keys.ENTER)