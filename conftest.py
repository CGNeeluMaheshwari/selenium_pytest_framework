import allure
import pytest
import os
from utils.driver_config import DriverConfig
from utils.config import Config
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    driver = DriverConfig.get_driver()
    driver.get(Config.BASE_URL)
    driver.maximize_window()

    # Instantiate the LoginPage and perform login using credentials from Config
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    request.cls.driver = driver
    yield driver
    driver.quit()


# Hook to capture screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshot_dir = os.path.join("reports","screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")

            allure.attach.file(screenshot_path,name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)



# browser-switching pytest setup using command-line options:
# import pytest
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")
#
# @pytest.fixture(scope="class")
# def setup_driver(request):
#     browser = request.config.getoption("--browser").lower()
#
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {browser}. Use 'chrome' or 'firefox'.")
#
#     request.cls.driver = driver
#     yield
#     driver.quit()
