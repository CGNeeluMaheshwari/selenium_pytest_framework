import pytest
from pages.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class TestProductPage:

    def test_add_product_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()

    def test_go_to_cart(self):
        product_page = ProductPage(self.driver)       
        product_page.go_to_cart()
        assert "cart.html" in self.driver.current_url, "Failed to add product to cart!"
