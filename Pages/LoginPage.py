from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage
from Utilities.Logger import Logger
from Utilities.dynamic_screenshot import Screenshot


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()
        #driver must be passed to initialize the Screenshot class
        self.screenshot = Screenshot(driver)

    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    femaleGender = (By.ID, "gender-ratio-2")
    stateId = (By.XPATH, "//div[contains(text(),'Select State')]")

    def enterFirstName(self, firstNameText):
        self.logger.info(f'Entering first: {firstNameText}')
        #we can take screenshot here by just passing the filename
        self.screenshot.take_screenshot("abcd")
        self.enter_text_into_element(self.firstName, firstNameText)

    def dummyClass(self):
        #we can take screenshot here by just passing the filename
        self.screenshot.take_screenshot("abcd")