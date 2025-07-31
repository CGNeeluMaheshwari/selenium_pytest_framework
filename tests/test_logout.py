import pytest
from pages.logout_page import LogoutPage


@pytest.mark.usefixtures("setup")
class TestLogoutPage:

    def test_logout(self):
        logout_page = LogoutPage(self.driver)
        logout_page.logout()