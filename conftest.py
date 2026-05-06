import pytest
from selenium import webdriver
from pages.login_page import  LoginPage
from config import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
