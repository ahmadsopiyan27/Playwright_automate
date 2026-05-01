import allure
from locators.login import Loc
from playwright.sync_api import expect


class Login:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        with allure.step('Input username'):
            self.driver.locator(Loc.input_username).fill(username)

    def input_password(self, password):
        with allure.step('Input password'):
            self.driver.locator(Loc.input_password).fill(password)

    def click_login_button(self):
        with allure.step('Click login button'):
            self.driver.locator(Loc.click_login_button).click()

    def verify_error_message(self, message):
        with allure.step('Verify error message'):
            expect(self.driver.locator(Loc.txt_error_message)).to_have_text(message)