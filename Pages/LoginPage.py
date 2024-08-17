from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from Utilities.Logger import Logger
from Utilities.static_screenshot import Screenshot


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()
        self.screenshot = Screenshot()

    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    femaleGender = (By.ID, "gender-ratio-2")
    stateId = (By.XPATH, "//div[contains(text(),'Select State')]")

    def enterFirstName(self, firstNameText):
        self.logger.info(f'Entering first: {firstNameText}')
        self.screenshot.take_screenshot(self.driver,"abcd")
        self.enter_text_into_element(self.firstName, firstNameText)
