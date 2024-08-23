import platform
import pytest
from selenium import webdriver
from Utilities.deleteLogs_and_screenShot import delete_logs_and_screenshots


@pytest.fixture()
def setup(request):

    current_os = str(platform.system())

    # Delete logs and screenshots before starting the tests
    delete_logs_and_screenshots()
    global driver

    try:
        if current_os == "Darwin":
            driver = webdriver.Safari()

        if current_os == 'Windows':
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        request.cls.driver = driver
        yield driver
        driver.quit()
    except Exception as e:
        print(str(e))
