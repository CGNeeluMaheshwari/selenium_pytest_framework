import pytest
from pages.product_page import ProductPage
from pages.cart_and_checkout_page import CartandCheckoutPage


@pytest.mark.usefixtures("setup")
class TestCheckoutPage:

    def test_add_product_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()

    def test_go_to_cart(self):
        product_page = ProductPage(self.driver)       
        product_page.go_to_cart()
        assert "cart.html" in self.driver.current_url, "Failed to add product to cart!"

    def test_checkout(self):
        cart_page = CartandCheckoutPage(self.driver)       
        cart_page.checkout()

    def test_enter_customer_info(self):
        checkout_page = CartandCheckoutPage(self.driver)
        checkout_page.enter_customer_info("Neelu", "Mahehswari", "560100")
        checkout_page.finish_checkout()
        assert "checkout-complete.html" in self.driver.current_url, "Checkout failed!"
        checkout_page.back_home()
