import platform
import pytest
from selenium import webdriver
from Utilities.cleanup_utility import cleanup_logs_and_screenshots


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use for tests")

@pytest.fixture()
def setup(request):
    # Clean up logs and screenshots before starting the test
    cleanup_logs_and_screenshots()

    global driver
    current_os = str(platform.system())
    browser = request.config.getoption("--browser").lower()

    #need to add step to pick browser from config file for all os.
    try:
        if current_os == "Darwin":
            driver = webdriver.Safari()

        if current_os == 'Windows':
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        request.cls.driver = driver
        yield driver

    except Exception as e:
        print(str(e))
