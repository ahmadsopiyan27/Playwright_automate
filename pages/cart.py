import allure
from playwright.sync_api import expect
from locators.cart import Loc


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        with allure.step('Open cart'):
            self.driver.locator(Loc.btn_cart).click()

    def verify_cart_page(self):
        with allure.step('Verify cart page'):
            expect(self.driver).to_have_url(Loc.url_cart)

    def click_checkout(self):
        with allure.step('Click checkout'):
            self.driver.locator(Loc.btn_checkout).click()