import allure
from playwright.sync_api import expect
from locators.checkout import Loc


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def input_information(self, firstname, lastname, postalcode):
        with allure.step('Input checkout information'):
            self.driver.locator(Loc.input_firstname).fill(firstname)
            self.driver.locator(Loc.input_lastname).fill(lastname)
            self.driver.locator(Loc.input_postalcode).fill(postalcode)
            self.driver.locator(Loc.btn_continue).click()

    def verify_overview_page(self):
        with allure.step('Verify checkout overview page'):
            expect(self.driver).to_have_url(Loc.url_overview)

    def finish_checkout(self):
        with allure.step('Finish checkout'):
            self.driver.locator(Loc.btn_finish).click()

    def verify_success_order(self, succes ):
        with allure.step('Verify order success'):
            expect(self.driver.locator(Loc.txt_success)).to_have_text(
                succes
            )