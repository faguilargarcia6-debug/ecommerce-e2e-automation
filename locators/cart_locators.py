from selenium.webdriver.common.by import By

class Cartlocator:
    CART_BUTTON = (By.CSS_SELECTOR, "a.toggle-drawer.cart.desktop")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.checkout")
    DRAWER = (By.ID, "drawer")
    