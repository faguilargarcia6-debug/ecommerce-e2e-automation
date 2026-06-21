from selenium.webdriver.support.ui import Select
from locators.products_locator import Productslocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from config import BASE_URL

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_product_page(self, product_slug):
        self.driver.get(BASE_URL + f"collections/frontpage/products/{product_slug}")

    def add_product_to_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//form[.//h1[contains(text(), '{product_name}')]]//input[@id='add']"
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_until_cart_updates(self):
        locator = (
            By.CSS_SELECTOR,
            ".cart-target"
        )

        self.wait.until(
            lambda driver:
            driver.find_element(*locator)
            .text.replace("(", "")
            .replace(")", "")
            .strip()
            .isdigit()
        )

        self.wait.until(
            lambda driver:
            int(
                driver.find_element(*locator)
                .text.replace("(", "")
                .replace(")", "")
                .strip()
            ) > 0
        )

    def wait_until_cart_count_is(self, expected_count):
        self.wait.until(
            lambda driver:
            int(
                driver.find_element(
                    *Productslocators.CART_COUNTER
                ).text.replace("(", "").replace(")", "")
            )
            == expected_count
        )

    def select_size(self, size):
        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(
                    Productslocators.SIZE_DROPDOWN
                )
            )
        )

        dropdown.select_by_visible_text(size)

    def select_color(self, color):
        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(
                    Productslocators.COLOR_DROPDOWN
                )
            )
        )

        dropdown.select_by_visible_text(color)

    def login_button_visible(self):
        return self.wait.until(EC.visibility_of_element_located(Productslocators.LOG_BUTTON_LOCATOR)).is_displayed()

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(Productslocators.LOG_BUTTON_LOCATOR)).click()