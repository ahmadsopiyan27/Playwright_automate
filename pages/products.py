import allure
from playwright.sync_api import expect
from locators.products import Loc   



class Products:
    def __init__(self, driver):
        self.driver = driver
    def check_url_products(self, url_products=Loc.txt_product):
        with allure.step('Verify inventory page'):
         expect(self.driver).to_have_url(url_products)

    def add_product_to_cart(self, product_name):
        with allure.step(f'Add product "{product_name}" to cart'):

            product_id = product_name.lower().replace(' ', '-')

            locator = f'xpath=//button[@id="add-to-cart-{product_id}"]'
            self.driver.locator(locator).click()
