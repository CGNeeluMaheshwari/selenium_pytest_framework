import logging

import pytest
from utils.config import Config
from utils.driver_config import DriverConfig
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def setup():
    logging.info("creating driver instance")
    # driver = DriverConfig.get_driver("chrome")
    driver = DriverConfig.get_driver()
    logging.info("get saucedemo web page")
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
def test_login(setup):
    print(" test login function start")
    login_page = LoginPage(setup)
    # login_page.login("standard_user", "secret_sauce")
    print("login page object created and passing user inputs ")
    login_page.login(Config.USERNAME, Config.PASSWORD)
    # Validate that the login is successful by checking the URL
    print("validating login page url")
    assert "inventory.html" in setup.current_url, "Login failed!"
    print("test login exit")




# import pytest
# from utils.data_loader import load_test_data
#
# test_data = load_test_data("test_data.json")
#
# @pytest.mark.parametrize("data", test_data)
# def test_login(driver, data):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element("id", "user-name").send_keys(data["username"])
#     driver.find_element("id", "password").send_keys(data["password"])
#     driver.find_element("id", "login-button").click()
#
#     if data["expected"] == "success":
#         assert "inventory" in driver.current_url
#     else:
#         error = driver.find_element("data-test", "error")
#         assert error.is_displayed()



# browser-switching pytest setup using command-line options:
# import pytest
# from selenium.webdriver.common.by import By
#
# @pytest.mark.usefixtures("setup_driver")
# class TestSample:
#     def test_open_google(self):
#         self.driver.get("https://www.google.com")
#         assert "Google" in self.driver.title
