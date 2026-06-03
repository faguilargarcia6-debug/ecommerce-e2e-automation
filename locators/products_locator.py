from selenium.webdriver.common.by import By

class Productslocators:
    SIZE_DROPDOWN = (By.ID, "product-select-option-0")
    COLOR_DROPDOWN = (By.ID, "product-select-option-1")
    LOG_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/account/login']")
    CART_COUNTER = (By.ID, "cart-target-desktop")
