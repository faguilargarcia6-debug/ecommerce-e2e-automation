import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_pages import CartPage
from pages.login_page import  LoginPage
from config import BASE_URL
from pages.products_pages import ProductsPage
from pages.checkout_pages import CheckoutPage

@pytest.fixture
def driver():
    options= Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver=webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def products_pages(driver):
    return ProductsPage(driver)

@pytest.fixture
def cart_pages(driver):
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)