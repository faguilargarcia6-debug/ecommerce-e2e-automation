from locators.locator_login import Loginlocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_URL

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)

    def open(self):
        self.driver.get(BASE_URL + '/account/login')

    def enter_email_address(self, email):
        element = self.wait.until(
            EC.visibility_of_element_located(Loginlocators.EMAIL_ADDRESS_LOCATOR)
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(Loginlocators.PASSWORD_LOCATOR)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(Loginlocators.LOGIN_BUTTON_LOCATOR)).click()

    def login(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(Loginlocators.MESSAGE_ERROR_LOCATOR)
        ).text

    def is_captcha_present(self):
        return "captcha" in self.driver.page_source.lower()

    def is_logged_in(self):
        return "/account" in self.driver.current_url