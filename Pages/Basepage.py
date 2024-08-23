import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BasePage:

    def enter_text_into_element(self, by_locator, text):
        self.logger.info(f'Entering text "{text}" into element by {by_locator}')
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator)).clear()
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
