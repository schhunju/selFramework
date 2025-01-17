import logging
import platform
from configparser import ConfigParser
from pathlib import Path
import pytest
from selenium import webdriver

global driver

@pytest.fixture(scope="function")
def driver_setup(request):
    current_os = str(platform.system())
    #need to add step to pick browser from config file for all os.
    try:
        if current_os == "Darwin":
            driver = webdriver.Chrome()

        if current_os == 'Windows':
            driver = webdriver.Chrome()

        driver.maximize_window()

        request.cls.driver = driver

        yield driver
        driver.quit()
        logging.info("Driver closed successfully.")
    except Exception as e:
        print(str(e))

def get_config_file_path():
    """
    This function returns the file path for the app-config.ini file located in the root directory.
    :return: the file path of the app-config.ini file by joining the root directory path with the file name.
    """
    project_name = "selFramework"
    script_path = Path(__file__).parent.parent
    final_path = Path.joinpath(script_path, "app-config.ini")
    return final_path

def get_config():
    """
    This function returns an instannce of the ConfigParser class.
    :return: 'ConfigParser' object.
    """
    return ConfigParser()

def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """
    parser.addoption("--environment", action="store", default="PP")

@pytest.fixture(scope="module")
def environment(request):
    """
    This is a Pytest fixture that returns the value of the command line option "--environment".

    :param request: 'request' is a built-in fixture in pytest that provides information about the test session and
    the current test being executed. It can be used to access command-line options, request additional fixtures, and
    perform other test-related operations. In this specific fixture, 'request' is used to retrieve the value of
    :return: A fixture name "ennvironment" is being returned. The fixture is defined using the pytest decorator
    "@pytest.fixture" and has a scope of "module". It takes a request object as an argument ad returns the value
    of the command line option "--environment" using the "request.config.getoption" method.
    """
    return request.config.getoption("--environment")

@pytest.fixture(scope="module")
def base_url(environment):
    """
    Fixture to provide "base_url" from the config file for a given environment.
    :param environment:
    :return:
    """
    configure = get_config()
    configure.read(get_config_file_path())
    return configure[environment]["base_url"]