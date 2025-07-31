# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
#
#
# class DriverConfig:
#     @staticmethod
#     def get_driver(browser_name="chrome"):
#         options = Options()
#         if browser_name == "chrome":
#             options.add_argument("--headless=new")
#             options.add_argument("--incognito")
#             driver = webdriver.Chrome(options=options)
#         elif browser_name == "firefox":
#             options.set_preference("browser.privatebrowsing.autostart", True)
#             driver = webdriver.Firefox(options=options)
#         else:
#             raise ValueError(f"Browser {browser_name} is not supported.")
#         return driver


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
#
#
# class DriverConfig:
#     @staticmethod
#     def get_driver(browser_name="chrome"):
#         if browser_name == "chrome":
#             options = ChromeOptions()
#             options.add_argument("--headless=new")
#             options.add_argument("--incognito")
#             driver = webdriver.Chrome(options=options)
#         elif browser_name == "firefox":
#             options = FirefoxOptions()
#             options.set_preference("browser.privatebrowsing.autostart", True)
#             driver = webdriver.Firefox(options=options)
#         else:
#             raise ValueError(f"Browser {browser_name} is not supported.")
#         return driver


import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DriverConfig:
    @staticmethod
    def get_driver(browser_name="chrome"):
        try:
            if browser_name.lower() == "chrome":
                options = ChromeOptions()
                options.add_argument("--headless=new")
                options.add_argument("--incognito")
                options.add_argument("--log-level=3")
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                logging.info("Launching Chrome browser...")
                driver = webdriver.Chrome(options=options)

            elif browser_name.lower() == "firefox":
                options = FirefoxOptions()
                options.set_preference("browser.privatebrowsing.autostart", True)
                logging.info("Launching Firefox browser...")
                driver = webdriver.Firefox(options=options)

            else:
                logging.error(f"Unsupported browser: {browser_name}")
                raise ValueError(f"Browser '{browser_name}' is not supported.")

            logging.info(f"{browser_name.capitalize()} browser launched successfully.")
            return driver

        except Exception as e:
            logging.exception("Failed to initialize the browser driver.")
            raise
