from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import BASE_URL
from locators.checkout_locator import CheckoutLocator



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_checkout_page(self):
        self.driver.get(BASE_URL + "/checkouts/cn/hWNAkzRMyZRh4gD1xpK2vcor/en-mx?_r=AQAB_K1didXCcp98w3UAmnFzHsh76Sq8VKCEvqjHJGh3MJ8")

    def guest_checkout_page(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutLocator.CHECKOUT_BUTTON)).click()

    def wait_for_checkout_page(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutLocator.PAY_BUTTON)).is_displayed()

    def user_as_guest(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutLocator.CONTACT_GUEST)).is_displayed()

    def invalid_card_tipe(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutLocator.INVALID_CARD)).is_displayed()

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.presence_of_element_located(CheckoutLocator.LAST_NAME)
        )
        element.clear()
        element.send_keys(last_name)

    def enter_address(self, address):
        element = self.wait.until(EC.visibility_of_element_located(CheckoutLocator.ADDRESS))
        element.clear()
        element.send_keys(address)

    def enter_postalcode(self, postalcode):
        element = self.wait.until(EC.visibility_of_element_located(CheckoutLocator.POSTCODE))
        element.clear()
        element.send_keys(postalcode)

    def enter_city(self, city):
        element = self.wait.until(EC.visibility_of_element_located(CheckoutLocator.CITY))
        element.clear()
        element.send_keys(city)

    def enter_rfc(self, rfc):
        element = self.wait.until(EC.visibility_of_element_located(CheckoutLocator.RFC))
        element.clear()
        element.send_keys(rfc)

    def select_state(self, state):
        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(
                    CheckoutLocator.STATE
                )
            )
        )

        dropdown.select_by_visible_text(state)

    def full_fill_data(self, data):
        self.enter_last_name(data['LASTNAME'])
        self.enter_address(data['ADDRESS'])
        self.enter_postalcode(data['POSTAL_CODE'])
        self.enter_city(data['CITY'])
        self.select_state(data['STATE'])

    def enter_card_number(self, card_number):
        iframe = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "iframe[id*='card-fields-number']"
                )
            )
        )

        self.driver.switch_to.frame(iframe)

        card_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "number")
            )
        )

        card_input.send_keys(card_number)

        self.driver.switch_to.default_content()

    def enter_expiry_date(self, expiry_date):
        iframe = self.wait.until(
            EC.presence_of_element_located(
                (
                    CheckoutLocator.EXPIRY_DATE
                )
            )
        )

        self.driver.switch_to.frame(iframe)

        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "expiry")
            )
        )

        element.send_keys("03")
        element.send_keys(Keys.TAB)
        element.send_keys("27")

        self.driver.switch_to.default_content()

    def enter_security_code(self, security_code):
        iframe = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "iframe[id*='card-fields-verification_value']"
                )
            )
        )

        self.driver.switch_to.frame(iframe)

        cvv_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "verification_value")
            )
        )

        cvv_input.send_keys(security_code)

        self.driver.switch_to.default_content()

    def enter_card_name(self, card_name):
        element = self.wait.until(EC.presence_of_element_located(CheckoutLocator.CARD_NAME))
        element.send_keys(card_name)

    def click_checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutLocator.PAY_BUTTON)).click()

    def payment_data(self, data):
        self.enter_card_number(data['CARD_NUMBER'])
        self.enter_expiry_date(data['EXPIRY_DATE'])
        self.enter_security_code(data['SECURITY_CODE'])
        self.enter_card_name(data['NAME_ON_CARD'])

    def enter_rfc(self, rfc):
        element = self.wait.until(EC.presence_of_element_located(CheckoutLocator.RFC))
        element.send_keys(rfc)


    def send_rfc(self, data):
        self.enter_rfc(data['RFC'])
        self.click_checkout_button()

    def enter_email(self, email):
        element = self.wait.until(EC.presence_of_element_located(CheckoutLocator.EMAIL))
        element.send_keys(email)

    def send_email(self, data):
        self.enter_email(data['EMAIL'])

    def last_name_error_visible(self):
        return self.wait.until(
            EC.presence_of_element_located(CheckoutLocator.LAST_NAME_ERROR)
        ).is_displayed()

    def address_error_visible(self):
        return self.wait.until(EC.presence_of_element_located(CheckoutLocator.ADDRESS_ERROR)).is_displayed()

    def postal_code_error_visible(self):
        return self.wait.until(EC.presence_of_element_located(CheckoutLocator.POSTCODE_ERROR)).is_displayed()

    def city_error_visible(self):
        return self.wait.until(EC.presence_of_element_located(CheckoutLocator.CITY_ERROR)).is_displayed()