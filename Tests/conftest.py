import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    global driver
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        request.cls.driver = driver
        yield driver
        driver.quit()
    except Exception as e:
        print(str(e))
