import allure
from playwright.sync_api import expect
from locators.products import Loc   



class Products:
    def __init__(self, driver):
        self.driver = driver
    def check_url_products(self, url_products=Loc.txt_product):
        with allure.step('Verify inventory page'):
         expect(self.driver).to_have_url(url_products)

    def add_product_to_cart(self):
        with allure.step('Add product to cart'):
            self.driver.locator('xpath=//button[@id="add-to-cart-sauce-labs-backpack"]').click()
