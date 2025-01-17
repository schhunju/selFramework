import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver_setup")
class BasePage:
    def clickElementByXpath(self, xpath):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    #
    # def enter_text_into_element(self, locator, text):
    #     self.driver.find_element(By.XPATH, locator).send_keys(text)