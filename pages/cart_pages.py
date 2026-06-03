from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from config import BASE_URL
from locators.cart_locators import Cartlocator


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_sauce(self):
        self.driver.get(BASE_URL)

    def open_cart_page(self):
        self.driver.get(BASE_URL + "/cart")

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                Cartlocator.CHECKOUT_BUTTON
            )
        ).click()

        self.wait.until(
            EC.url_contains("/cart")
        )

    def is_product_in_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//a[contains(., '{product_name}')]"
        )

        products = self.driver.find_elements(*locator)

        return len(products) > 0

    def product_variant_is_displayed(
            self,
            product_name,
            size,
            color
    ):
        expected_variant = f"{product_name} - {size} / {color}"

        locator = (
            By.XPATH,
            f"//a[contains(., '{expected_variant}')]"
        )

        variants = self.driver.find_elements(*locator)

        return len(variants) > 0

    def remove_product(self, product_name):
        locator = (
            By.XPATH,
            f"//div[@class='row'][.//h3/a[contains(text(), '{product_name}')]]//div[contains(@class,'remove')]//a"
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def cart_dropdown(self):
        self.wait.until(
            EC.element_to_be_clickable(Cartlocator.CART_BUTTON)
        ).click()

    def is_cart_dropdown_visible(self):
        drawer = self.wait.until(
            EC.presence_of_element_located(
                Cartlocator.DRAWER
            )
        )

        return drawer.is_displayed()

    def cart_content_is_displayed(self):

        return len(
            self.driver.find_elements(
                By.CSS_SELECTOR,
                "#drawer form[action='/cart']"
            )
        ) > 0

    def get_product_price(self, product_name):

        locator = (
            By.XPATH,
            f"//div[contains(@class,'row')][.//a[contains(., '{product_name}')]]//div[contains(@class,'price')]"
        )

        elements = self.driver.find_elements(*locator)

        for element in elements:

            text = element.text.strip()

            if text:
                return float(
                    text.replace("£", "")
                )

        raise Exception(
            f"No valid price found for product: {product_name}"
        )

    def get_cart_total(self):
        total_text = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cart.total h2")
            )
        ).text

        return float(
            total_text
            .replace("Total", "")
            .replace("£", "")
            .strip()
        )

    def wait_for_cart_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cart.total h2")
            )
        )