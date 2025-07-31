from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutPage(BasePage):
    NAVIGATION_ICON = (By.XPATH,'//*[@id="menu_button_container"]/div/div[1]/div')
    LOGOUT = (By.XPATH,'//*[@id="logout_sidebar_link"]')

    def logout(self):
        self.click(self.NAVIGATION_ICON)
        self.click(self.LOGOUT)
