import allure
from pages.login import Login
from pages.products import Products
from pages.cart import Cart
from pages.checkout import Checkout
import pytest



@pytest.mark.parametrize(
    "product_name",
    [
        pytest.param('Sauce Labs Backpack', id="backpack"),
        pytest.param('Sauce Labs Bike Light', id="bike"),
        pytest.param('Sauce Labs Bolt T-Shirt', id="tshirt"),
        pytest.param('Sauce Labs Fleece Jacket', id="jacket"),
        pytest.param('Sauce Labs Onesie', id="onesie"),
        pytest.param('Test.allTheThings() T-Shirt (Red)', id="red_tshirt"),
    ]
)

@allure.title('End to End Checkout')
@allure.description('Login, add product to cart, checkout until order success')
@allure.severity(allure.severity_level.CRITICAL)
def test_end_to_end_checkout(setup, product_name):


    login = Login(setup)
    product = Products(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)

    # Login
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()


    # Add to cart
    product.add_product_to_cart(product_name)

    # Cart
    cart.open_cart()
    cart.click_checkout()

    # Checkout
    checkout.input_information('Ahmad', 'Sofiyan', '12345')
    checkout.verify_overview_page()
    checkout.finish_checkout()
    checkout.verify_success_order('Thank you for your order!')