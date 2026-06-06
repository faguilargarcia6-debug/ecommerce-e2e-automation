import pytest

from conftest import products_pages, cart_pages


@pytest.mark.products
class TestProducts:
    def test_add_to_cart_button_works(self, products_pages, cart_pages):

        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart()

        assert cart_pages.is_product_in_cart("Noir jacket")

    def test_user_can_add_products_to_cart_as_guest(self, products_pages, cart_pages):

        products_pages.open_product_page("noir-jacket")

        assert products_pages.login_button_visible()

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart()

        assert cart_pages.is_product_in_cart("Noir jacket")

    def test_user_can_select_size_and_color(self, products_pages, cart_pages):

        products_pages.open_product_page("noir-jacket")

        products_pages.select_size("S")
        products_pages.select_color("Blue")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart()

        assert cart_pages.product_variant_is_displayed(
            "Noir jacket",
            size= "S",
            color= "Blue",
        )
