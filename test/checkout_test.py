import pytest

from data.checkout_data import SHIPPING_INFORMATION, INVALID_CARD, LAST_DATA, FIRST_DATA


@pytest.mark.checkout
class TestCheckout:
    def test_checkout_without_log_in(self, products_pages, cart_pages, checkout_page):

        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        assert products_pages.login_button_visible()

        checkout_page.guest_checkout_page()

        assert checkout_page.user_as_guest(), (
            "user checkout as guest."
        )

    def test_last_name_field_must_be_complete(self, checkout_page, cart_pages, products_pages):
        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        checkout_page.guest_checkout_page()

        checkout_page.wait_for_checkout_page()

        data = SHIPPING_INFORMATION.copy()
        data["LASTNAME"] = ""

        checkout_page.full_fill_data(data)

        checkout_page.send_rfc(LAST_DATA)

        assert checkout_page.last_name_error_visible()

    def test_address_field_must_be_complete(self, checkout_page, cart_pages, products_pages):
        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        checkout_page.guest_checkout_page()

        checkout_page.wait_for_checkout_page()

        data = SHIPPING_INFORMATION.copy()
        data["ADDRESS"] = ""

        checkout_page.full_fill_data(data)

        checkout_page.send_rfc(LAST_DATA)

        assert checkout_page.address_error_visible()

    def test_postal_code_field_must_be_complete(self, checkout_page, cart_pages, products_pages):
        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        checkout_page.guest_checkout_page()

        checkout_page.wait_for_checkout_page()

        data = SHIPPING_INFORMATION.copy()
        data["POSTAL_CODE"] = ""

        checkout_page.full_fill_data(data)

        checkout_page.click_checkout_button()

        assert checkout_page.postal_code_error_visible()

    def test_city_field_must_be_complete(self, checkout_page, cart_pages, products_pages):
        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        checkout_page.guest_checkout_page()

        checkout_page.wait_for_checkout_page()

        data = SHIPPING_INFORMATION.copy()
        data["CITY"] = ""

        checkout_page.full_fill_data(data)

        checkout_page.send_rfc(LAST_DATA)

        assert checkout_page.city_error_visible()

    def test_user_can_not_pay_with_invalid_card(self, products_pages, cart_pages, checkout_page, login_page):

        products_pages.open_product_page("noir-jacket")

        products_pages.add_product_to_cart("Noir jacket")

        products_pages.wait_until_cart_updates()

        cart_pages.open_cart_page()

        checkout_page.guest_checkout_page()

        checkout_page.wait_for_checkout_page()

        checkout_page.full_fill_data(SHIPPING_INFORMATION)

        checkout_page.payment_data(INVALID_CARD)

        checkout_page.send_email(FIRST_DATA)

        checkout_page.send_rfc(LAST_DATA)

        assert checkout_page.invalid_card_tipe()



    @pytest.mark.skip(reason= "BUG=002 BLOCKS CHECKOUT VALIDATION")
    def test_user_can_complete_purchase_with_valid_card(self, checkout_page):
        pass
    @pytest.mark.skip(reason= "BUG=002 BLOCKS CHECKOUT VALIDATION")
    def test_user_can_pay_with_valid_card_types(self):
        pass

