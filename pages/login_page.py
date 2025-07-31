from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    ERROR_MESSAGE = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

    def login(self,username,password):
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)