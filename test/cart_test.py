import pytest
from selenium.webdriver.support.wait import time
@pytest.mark.cart
class TestCart:

    def test_cart_button_displays_cart_dropdown(self, cart_pages):

        cart_pages.open_sauce()

        cart_pages.cart_dropdown()

        assert cart_pages.is_cart_dropdown_visible()

    @pytest.mark.xfail(
        reason="BUG-1: Cart drawer content does not refresh after adding products."
    )
    def test_cart_button_displays_added_products(self, cart_pages, products_pages):

        products_pages.open_product_page("noir-jacket")

        cart_pages.cart_dropdown()

        products_pages.add_product_to_cart("Noir jacket")

        assert cart_pages.cart_content_is_displayed(), (
            "Cart drawer did not refresh after adding a product."
        )
    def test_cart_keep_product_after_log_in(self, cart_pages, products_pages, login_page):

        products_pages.open_product_page("noir-jacket")

        assert products_pages.login_button_visible()

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        products_pages.click_login_button()

        login_page.login("Iguanabel@gmail.com", "Iguanabel")

        cart_pages.open_cart()

        assert cart_pages.is_product_in_cart(
            "Noir jacket")

    def test_user_can_delete_product(self, cart_pages,products_pages):

        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart()

        assert cart_pages.is_product_in_cart("Noir jacket")

        cart_pages.remove_product("Noir jacket")

        assert not cart_pages.is_product_in_cart("Noir jacket")

    def test_cart_total_is_calculated_correctly(self, products_pages, cart_pages):
        #Total excludes shipping cost and taxes.

        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        products_pages.open_product_page("grey-jacket")

        products_pages.add_product_to_cart("Grey jacket")

        products_pages.wait_until_cart_count_is(2)

        cart_pages.open_cart_page()

        cart_pages.wait_for_cart_page()

        expected_total = (
                cart_pages.get_product_price("Noir jacket")
                +
                cart_pages.get_product_price("Grey jacket")
        )

        actual_total = cart_pages.get_cart_total()

        assert actual_total == expected_total