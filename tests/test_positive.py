import pytest
import allure
from pages import login
from pages.login import Login
from pages.products import Products
from tests.conftest import setup


@allure.title('Login Positif')
@allure.description('Login with valid username and password')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_positif(setup):
    
        login = Login(setup)

        login.input_username('standard_user')
        login.input_password('secret_sauce')
        login.click_login_button()

        Products(setup).check_url_products('https://www.saucedemo.com/inventory.html')
