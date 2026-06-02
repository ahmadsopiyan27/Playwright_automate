import pytest
import allure
from pages import login
from pages.login import Login
from pages.products import Products
from tests.conftest import setup
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")


@allure.title('Login Positif')
@allure.description('Login with valid username and password')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_positif1(setup):
    
        login = Login(setup)

        login.input_username(username)
        login.input_password(password)
        login.click_login_button()

        Products(setup).check_url_products('https://www.saucedemo.com/inventory.html')
