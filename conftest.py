import pytest
from selenium import webdriver

from pages.cart_pages import CartPage
from pages.login_page import  LoginPage
from config import BASE_URL
from pages.products_pages import ProductsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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