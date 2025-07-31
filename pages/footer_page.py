import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class FooterPage(BasePage):
    TWITTER = (By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    FACEBOOK = (By.XPATH,'//*[@id="pagepage_wrapper"]/footer/ul/li[2]/a')
    lINKEDIN = (By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[3]/a')
    
    def scroll_to_footer(self):
        footer_element = self.driver.find_element(By.XPATH, '//*[@id="page_wrapper"]/footer')
        ActionChains(self.driver).move_to_element(footer_element).perform()
    

    def social_media_link(self):
        self.scroll_to_footer()
        original_window = self.driver.current_window_handle 
        self.click(self.lINKEDIN)
        time.sleep(10)

         # Wait for the new window or tab to open
        new_window_handles = self.driver.window_handles  # Get list of window handles
        for handle in new_window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)  # Switch to the new tab
                break

        # Verify LinkedIn tab is opened
        assert "LinkedIn" in self.driver.title, "LinkedIn page"

        # Close the new tab and switch back to the original window
        self.driver.close()
        self.driver.switch_to.window(original_window)
        