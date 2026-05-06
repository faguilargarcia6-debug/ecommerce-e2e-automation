from selenium.webdriver.common.by import By

class Loginlocators:
    EMAIL_ADDRESS_LOCATOR = (By.ID, "customer_email")
    PASSWORD_LOCATOR = (By.ID, "customer_password")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input[value='Sign In']")
    MESSAGE_ERROR_LOCATOR = (By.CSS_SELECTOR, ".errors li")
    

