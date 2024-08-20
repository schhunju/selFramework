import platform
import pytest
from selenium import webdriver
from Utilities.delete_logs_and_screenshots import delete_logs_and_screenshots

@pytest.fixture(scope="session", autouse=True)
def setup(request):
    
    # Delete logs and screenshots before starting the tests
    delete_logs_and_screenshots()

    global driver
    current_os = str(platform.system())
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
        driver.quit()
    except Exception as e:
        print(str(e))
