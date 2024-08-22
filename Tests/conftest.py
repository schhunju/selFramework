# import platform
# import pytest
# from selenium import webdriver
# from Utilities.delete_logs_and_screenshots import delete_logs_and_screenshots
#
# @pytest.fixture(scope="session", autouse=True)
#
# def setup(request):
#
#     # Delete logs and screenshots before starting the tests
#     delete_logs_and_screenshots()
#
#     global driver
#     current_os = str(platform.system())
#     #need to add step to pick browser from config file for all os.
#     try:
#         if current_os == "Darwin":
#             driver = webdriver.Safari()
#
#         if current_os == 'Windows':
#             driver = webdriver.Chrome()
#
#         driver.maximize_window()
#         driver.get("https://demoqa.com/automation-practice-form")
#         request.cls.driver = driver
#         yield driver
#         driver.quit()
#     except Exception as e:
#         print(str(e))
import platform
import pytest
from selenium import webdriver
from Utilities.delete_logs_and_screenshots import delete_logs_and_screenshots

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    # Delete logs and screenshots before starting the tests
    delete_logs_and_screenshots()

    # Browser initialization based on OS
    current_os = platform.system()

    try:
        if current_os == "Darwin":
            driver = webdriver.Safari()
        elif current_os == 'Windows':
            driver = webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported OS: {current_os}")

        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        request.cls.driver = driver
        yield driver

    except Exception as e:
        print(f"Error during setup: {str(e)}")
        raise  # Re-raise the exception to prevent tests from running

    finally:
        driver.quit()
