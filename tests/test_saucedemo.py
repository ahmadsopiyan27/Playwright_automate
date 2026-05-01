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

        login.input_usernamee('standard_user')
        login.input_password('secret_sauce')
        login.click_login_button()

        Products(setup).check_url_products('https://www.saucedemo.com/inventory.html')

        
# # data parametrize
# data_login = [
#     ('standard_user', 'salah', 'Epic sadface: Username and password do not match any user in this service'),
#     ('salah_user', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
#     ('', 'secret_sauce', 'Epic sadface: Username is required'),
#     ('standard_user', '', 'Epic sadface: Password is required'),
#     ('', '', 'Epic sadface: Username is required')
# ]


# @allure.title('Login Negatif')
# @allure.description('Login menggunakan credential yang tidak valid')
# @allure.severity(allure.severity_level.NORMAL)
# @pytest.mark.parametrize('username, password, error_message', data_login)
# def test_login_negatif(username, password, error_message):

#     '''Test Case 2 login using invalid credentials'''

#     with sync_playwright() as p:
#         with allure.step('Open browser'):
#             browser = p.chromium.launch(headless=False)
#             page = browser.new_page()

#         with allure.step('Open SauceDemo'):
#             page.goto('https://www.saucedemo.com/')

#         with allure.step('Input credential'):
#             page.locator('xpath=//input[@id="user-name"]').fill(username)
#             page.locator('xpath=//input[@id="password"]').fill(password)
#             page.locator('xpath=//input[@id="login-button"]').click()

#         with allure.step('Verify error message'):
#             expect(
#                 page.locator('xpath=//h3[@data-test="error"]')
#             ).to_have_text(error_message)

#         browser.close()


# @allure.title('End to End Checkout')
# @allure.description('Login, add product to cart, checkout until order success')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_end_to_end_checkout():
#     '''Test Case 3 End to End Checkout'''

#     with sync_playwright() as p:
#         with allure.step('Open browser'):
#             browser = p.chromium.launch(headless=False)
#             page = browser.new_page()

#         with allure.step('Open SauceDemo'):
#             page.goto('https://www.saucedemo.com/')

#         with allure.step('Login with valid credentials'):
#             page.locator('xpath=//input[@id="user-name"]').fill('standard_user')
#             page.locator('xpath=//input[@id="password"]').fill('secret_sauce')
#             page.locator('xpath=//input[@id="login-button"]').click()

#         with allure.step('Verify inventory page'):
#             expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

#         with allure.step('Add product to cart'):
#             page.locator('xpath=//button[@id="add-to-cart-sauce-labs-backpack"]').click()

#         with allure.step('Open cart'):
#             page.locator('xpath=//a[@class="shopping_cart_link"]').click()

#         with allure.step('Verify cart page'):
#             expect(page).to_have_url('https://www.saucedemo.com/cart.html')

#         with allure.step('Click checkout'):
#             page.locator('xpath=//button[@id="checkout"]').click()

#         with allure.step('Input checkout information'):
#             page.locator('xpath=//input[@id="first-name"]').fill('Ahmad')
#             page.locator('xpath=//input[@id="last-name"]').fill('Sofiyan')
#             page.locator('xpath=//input[@id="postal-code"]').fill('12345')
#             page.locator('xpath=//input[@id="continue"]').click()

#         with allure.step('Verify checkout overview page'):
#             expect(page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')

#         with allure.step('Finish checkout'):
#             page.locator('xpath=//button[@id="finish"]').click()

#         with allure.step('Verify order success'):
#             expect(page.locator('xpath=//h2[@class="complete-header"]')).to_have_text(
#                 'Thank you for your order!'
#             )

#         browser.close()