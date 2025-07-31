import pytest
from pages.footer_page import FooterPage


@pytest.mark.usefixtures("setup")
class TestFooterPage:
    def test_social_media_link(self):
        footer_page = FooterPage(self.driver)
        footer_page.social_media_link()